#!/usr/bin/env python3
"""
Kahoot API - Simplified version based on original Kitty-Tools src/client.py
"""

import json
import re
import ssl
import time
import random
import urllib.request
import urllib.error


class SSLContextManager:
    """Handle SSL certificate issues across platforms"""
    
    @staticmethod
    def create_ssl_context():
        """Create SSL context with fallback for certificate issues"""
        try:
            return ssl.create_default_context()
        except Exception:
            return ssl._create_unverified_context()


class RateLimiter:
    """Rate limiter to avoid getting blocked"""
    
    def __init__(self, min_delay=1.0, max_delay=3.0):
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.last_request = None
    
    def wait(self):
        """Wait appropriate time between requests"""
        if self.last_request:
            elapsed = time.time() - self.last_request
            delay = random.uniform(self.min_delay, self.max_delay)
            
            if elapsed < delay:
                sleep_time = delay - elapsed
                time.sleep(sleep_time)
        
        self.last_request = time.time()


class KahootAPI:
    """Kahoot API client - simplified version"""
    
    BASE_API_URL = "https://play.kahoot.it/rest/kahoots/"
    CHALLENGE_API_URL = "https://kahoot.it/rest/challenges/pin/"
    REQUEST_TIMEOUT = 15
    
    def __init__(self):
        self.rate_limiter = RateLimiter()
        self.ssl_context = SSLContextManager.create_ssl_context()
    
    def _get_headers(self):
        """Generate realistic browser headers"""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        
        return {
            'User-Agent': random.choice(user_agents),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Cache-Control': 'no-cache'
        }
    
    def _make_request(self, url, max_retries=3):
        """Make request with retry logic and proper error handling"""
        for attempt in range(max_retries):
            try:
                # Apply rate limiting
                self.rate_limiter.wait()
                
                # Create request with headers
                headers = self._get_headers()
                request = urllib.request.Request(url, headers=headers)
                
                # Make the request with SSL context
                with urllib.request.urlopen(request, timeout=self.REQUEST_TIMEOUT, context=self.ssl_context) as response:
                    return json.loads(response.read().decode('utf-8'))
                    
            except urllib.error.HTTPError as e:
                if e.code == 403:
                    if attempt < max_retries - 1:
                        wait_time = (attempt + 1) * 5
                        time.sleep(wait_time)
                        continue
                    else:
                        return {'error': 'Access forbidden. This could be due to rate limiting or geographic restrictions.'}
                
                elif e.code == 404:
                    return {'error': 'Quiz not found. Please verify the Quiz ID is correct.'}
                
                elif e.code == 429:  # Too Many Requests
                    if attempt < max_retries - 1:
                        wait_time = (attempt + 1) * 10
                        time.sleep(wait_time)
                        continue
                    else:
                        return {'error': 'Rate limited by server. Please wait a few minutes and try again.'}
                
                else:
                    return {'error': f'HTTP Error {e.code}: {e.reason}'}
                    
            except urllib.error.URLError as e:
                return {'error': f'Connection error: {e.reason}. Check your internet connection.'}
                
            except ssl.SSLError as e:
                if attempt < max_retries - 1:
                    # Try with unverified context on next attempt
                    self.ssl_context = ssl._create_unverified_context()
                    continue
                else:
                    return {'error': f'SSL connection failed: {e}'}
                    
            except json.JSONDecodeError:
                return {'error': 'Failed to parse the response from Kahoot servers.'}
                
            except Exception as e:
                if attempt < max_retries - 1:
                    time.sleep(2)
                    continue
                else:
                    return {'error': f'Unexpected error: {str(e)}'}
        
        return {'error': 'All retry attempts failed'}
    
    @staticmethod
    def get_quiz_by_id(quiz_id):
        """Get quiz by ID - static method like original"""
        if not re.fullmatch(r"^[A-Za-z0-9-]*$", quiz_id):
            return {'error': False}
        
        api = KahootAPI()
        url = f"{api.BASE_API_URL}{quiz_id}"
        return api._make_request(url)
    
    @staticmethod
    def get_quiz_id_from_pin(pin):
        """Convert PIN to Quiz ID - static method like original"""
        if not pin.isdigit():
            return {'error': 'PIN must contain only digits'}
            
        api = KahootAPI()
        url = f"{api.CHALLENGE_API_URL}{pin}"
        result = api._make_request(url)
        
        if 'error' not in result and 'id' in result:
            return {'quiz_id': result['id']}
        elif 'error' not in result:
            return {'error': 'No quiz ID found in response'}
        
        return result


class Kahoot:
    """Kahoot quiz class - simplified version"""
    
    def __init__(self, uuid):
        self.uuid = uuid
        try:
            if not re.fullmatch(r"^[A-Za-z0-9-]*$", uuid):
                self.data = False
            else:
                self.data = self._fetch_quiz_data(uuid)
        except:
            self.data = False

    def _fetch_quiz_data(self, uuid):
        """Fetch quiz data"""
        result = KahootAPI.get_quiz_by_id(uuid)
        if 'error' in result:
            return False
        return result

    def get_quiz_details(self):
        """Get quiz details"""
        if not self.data:
            return None
        return {
            "uuid": self.data["uuid"],
            "creator_username": self.data.get("creator_username", "Unknown"),
            "title": self.data.get("title", "Untitled Quiz"),
            "description": self.data.get("description", ""),
            "cover": self.data.get("cover", "")
        }

    def get_questions(self):
        """Get questions"""
        if not self.data:
            return []
        return self.data.get("questions", [])

    def get_quiz_length(self):
        """Get number of questions"""
        if not self.data:
            return 0
        return len(self.data.get("questions", []))

    def get_question_details(self, question):
        """Get question details"""
        if not self.data or question >= self.get_quiz_length():
            return None
            
        q = self.data["questions"][question]
        question_type = q.get("type", "unknown")
        
        if question_type == "content":
            data = {
                "type": "content",
                "title": self._clean_text(q.get("title", "")),
                "description": self._clean_text(q.get("description", ""))
            }
        else:
            data = {
                "type": question_type,
                "question": self._clean_text(q.get("question", "")),
                "choices": q.get("choices", []),
                "amount_of_answers": len(q.get("choices", [])),
                "amount_of_correct_answers": 0
            }
            
            # Clean choices and count correct answers
            for i, choice in enumerate(data["choices"]):
                data["choices"][i]["answer"] = self._clean_text(choice.get("answer", ""))
                if choice.get("correct", False):
                    data["amount_of_correct_answers"] += 1

        return data

    def get_answer(self, question):
        """Get answers for question"""
        details = self.get_question_details(question)
        
        if not details or details["type"] == "content":
            return None
            
        answers = []
        
        if details["type"] == "jumble":
            for choice in details["choices"]:
                answers.append(choice["answer"])
        else:
            for choice in details["choices"]:
                if choice.get("correct", False):
                    answers.append(choice["answer"])
                    
        return answers if answers else None

    def _clean_text(self, text):
        """Clean HTML and formatting from text"""
        if not text:
            return ""
            
        text = str(text)
        
        # Remove HTML tags
        replacements = [
            ("<p>", ""), ("</p>", ""), 
            ("<strong>", ""), ("</strong>", ""),
            ("<b>", ""), ("</b>", ""),
            ("<br/>", "\n"), ("<br>", "\n"),
            ("<span>", ""), ("</span>", ""),
            ("<math>", ""), ("</math>", ""),
            ("<semantics>", ""), ("</semantics>", ""),
            ("<mrow>", ""), ("</mrow>", ""),
            ("<mo>", ""), ("</mo>", ""),
            ("<msup>", ""), ("</msup>", ""),
            ("<mi>", ""), ("</mi>", ""),
            ("<mn>", ""), ("</mn>", ""),
            ("<annotation>", ""), ("</annotation>", "")
        ]
        
        for old, new in replacements:
            text = text.replace(old, new)
        
        # Remove any remaining HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        return text.strip()


def start_kahoot(quiz_input):
    """
    Main function to get kahoot quiz - simplified version
    """
    # Normalize PIN input (remove spaces, dashes, etc.)
    if quiz_input and not quiz_input.isalnum():
        # Remove common separators for PIN
        normalized = quiz_input.replace(' ', '').replace('-', '').replace('.', '')
        if normalized.isdigit():
            quiz_input = normalized
    
    try:
        # Check if input is PIN or Quiz ID
        if quiz_input.isdigit():
            # It's a PIN, convert to Quiz ID
            result = KahootAPI.get_quiz_id_from_pin(quiz_input)
            
            if 'error' in result:
                return None, f"Error: {result['error']}\n\nNote: PIN only works when game is active."
            
            quiz_id = result['quiz_id']
        else:
            # It's a Quiz ID
            quiz_id = quiz_input
        
        # Get quiz data
        kahoot = Kahoot(quiz_id)
        
        if not kahoot.data:
            return None, "Failed to fetch quiz data. Please check the Quiz ID and try again."
        
        return kahoot, None
        
    except Exception as e:
        return None, f"An error occurred: {str(e)}"