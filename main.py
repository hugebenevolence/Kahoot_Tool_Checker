"""
Kahoot Quiz Viewer - Simple Extension
GUI đơn giản để xem câu hỏi và đáp án từ Kahoot
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
from kahoot_api import start_kahoot


class KahootViewer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Kahoot Quiz Viewer")
        self.root.geometry("900x700")
        self.root.configure(bg="#2c3e50")
        
        self.setup_gui()
        
    def setup_gui(self):
        """Setup the main GUI components"""
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#2c3e50", padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="Kahoot Quiz Viewer", 
            font=("Arial", 18, "bold"),
            bg="#2c3e50", 
            fg="#ecf0f1"
        )
        title_label.pack(pady=(0, 20))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg="#2c3e50")
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Input label
        input_label = tk.Label(
            input_frame,
            text="Nhập Quiz ID hoặc Game PIN:",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        input_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Help label
        help_label = tk.Label(
            input_frame,
            text="• Quiz ID: chuỗi ký tự (vd: f47ac10b-58cc-4372-a567-0e02b2c3d479)\n• Game PIN: 6-7 chữ số, có thể có khoảng trắng (vd: 735 0114)\n• PIN chỉ hoạt động khi game đang diễn ra",
            font=("Arial", 9),
            bg="#2c3e50",
            fg="#95a5a6",
            justify=tk.LEFT
        )
        help_label.pack(anchor=tk.W, pady=(0, 10))
        
        # Input entry and button frame
        entry_frame = tk.Frame(input_frame, bg="#2c3e50")
        entry_frame.pack(fill=tk.X)
        
        # Input entry
        self.quiz_input = tk.Entry(
            entry_frame,
            font=("Arial", 12),
            bg="#34495e",
            fg="#ecf0f1",
            insertbackground="#ecf0f1",
            relief=tk.FLAT,
            bd=5
        )
        self.quiz_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.quiz_input.bind("<Return>", lambda e: self.fetch_quiz())
        
        # Fetch button
        self.fetch_button = tk.Button(
            entry_frame,
            text="Tải Quiz",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="#ecf0f1",
            relief=tk.FLAT,
            bd=0,
            padx=20,
            command=self.fetch_quiz,
            cursor="hand2"
        )
        self.fetch_button.pack(side=tk.RIGHT)
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Sẵn sàng. Nhập Quiz ID hoặc Game PIN để bắt đầu.",
            font=("Arial", 10),
            bg="#2c3e50",
            fg="#95a5a6"
        )
        self.status_label.pack(pady=(0, 10))
        
        # Results frame with scrollbar
        results_frame = tk.Frame(main_frame, bg="#2c3e50")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        # Results text area with scrollbar
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            font=("Consolas", 10),
            bg="#34495e",
            fg="#ecf0f1",
            insertbackground="#ecf0f1",
            relief=tk.FLAT,
            bd=5,
            wrap=tk.WORD,
            state=tk.DISABLED
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
        # Footer
        footer_frame = tk.Frame(main_frame, bg="#2c3e50")
        footer_frame.pack(fill=tk.X, pady=(10, 0))
        
        footer_label = tk.Label(
            footer_frame,
            text="Kitty-Tools Extension - Đơn giản và hiệu quả",
            font=("Arial", 9),
            bg="#2c3e50",
            fg="#7f8c8d"
        )
        footer_label.pack()
        
    def update_status(self, message, color="#95a5a6"):
        """Update status message"""
        self.status_label.configure(text=message, fg=color)
        
    def clear_results(self):
        """Clear the results text area"""
        self.results_text.configure(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.configure(state=tk.DISABLED)
        
    def display_results(self, kahoot):
        """Display quiz questions and answers"""
        self.results_text.configure(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        
        # Quiz info
        quiz_details = kahoot.get_quiz_details()
        
        info_text = f"""╔═══════════════════════════════════════════════════════════════╗
║                          THÔNG TIN QUIZ                          ║
╠═══════════════════════════════════════════════════════════════╣
║ Tiêu đề: {quiz_details['title'][:50]}{'...' if len(quiz_details['title']) > 50 else ''}
║ Tác giả: {quiz_details['creator_username']}
║ Số câu hỏi: {kahoot.get_quiz_length()}
║ Quiz ID: {quiz_details['uuid']}
╚═══════════════════════════════════════════════════════════════╝

"""
        
        if quiz_details['description']:
            info_text += f"Mô tả: {quiz_details['description']}\n\n"
        
        self.results_text.insert(tk.END, info_text)
        
        # Questions and answers
        for i in range(kahoot.get_quiz_length()):
            question_details = kahoot.get_question_details(i)
            
            if not question_details:
                continue
                
            if question_details['type'] == 'content':
                # Content slide
                question_text = f"┌─ CÂU HỎI {i+1} ─ CONTENT SLIDE ─\n"
                question_text += f"│ {question_details['title']}\n"
                if question_details['description']:
                    question_text += f"│ Mô tả: {question_details['description']}\n"
                question_text += "└" + "─" * 60 + "\n\n"
            else:
                # Regular question
                question_text = f"┌─ CÂU HỎI {i+1} ─ {question_details['type'].upper()} ─\n"
                question_text += f"│ {question_details['question']}\n│\n"
                
                # Show all choices if available
                if question_details.get('choices'):
                    question_text += "│ Các lựa chọn:\n"
                    answers = kahoot.get_answer(i) or []
                    
                    for j, choice in enumerate(question_details['choices'], 1):
                        answer_text = choice.get('answer', f'Choice {j}')
                        marker = "●" if choice.get('correct', False) else "○"
                        question_text += f"│   {marker} {j}. {answer_text}\n"
                    question_text += "│\n"
                    
                    # Correct answers
                    if answers:
                        question_text += "│ ✓ Đáp án đúng:\n"
                        for answer in answers:
                            question_text += f"│   → {answer}\n"
                
                question_text += "└" + "─" * 60 + "\n\n"
            
            self.results_text.insert(tk.END, question_text)
        
        self.results_text.configure(state=tk.DISABLED)
        
        # Scroll to top
        self.results_text.see(1.0)
        
    def fetch_quiz_thread(self, quiz_input):
        """Fetch quiz data in separate thread to avoid freezing GUI"""
        try:
            # Update status
            self.root.after(0, lambda: self.update_status("Đang tải dữ liệu quiz...", "#f39c12"))
            self.root.after(0, lambda: self.fetch_button.configure(state=tk.DISABLED, text="Đang tải..."))
            
            # Fetch quiz using simplified API
            kahoot, error = start_kahoot(quiz_input)
            
            if error:
                # Show error
                self.root.after(0, lambda: self.update_status(f"Lỗi: {error}", "#e74c3c"))
                self.root.after(0, self.clear_results)
            else:
                # Display results
                self.root.after(0, lambda: self.display_results(kahoot))
                self.root.after(0, lambda: self.update_status("Tải thành công!", "#27ae60"))
                
        except Exception as e:
            self.root.after(0, lambda: self.update_status(f"Lỗi không xác định: {str(e)}", "#e74c3c"))
            
        finally:
            # Re-enable button
            self.root.after(0, lambda: self.fetch_button.configure(state=tk.NORMAL, text="Tải Quiz"))
            
    def fetch_quiz(self):
        """Main function to fetch quiz"""
        quiz_input = self.quiz_input.get().strip()
        
        if not quiz_input:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập Quiz ID hoặc Game PIN!")
            return
        
        # Warning for PIN input
        normalized_input = quiz_input.replace(' ', '').replace('-', '')
        if normalized_input.isdigit():
            result = messagebox.askyesno(
                "Xác nhận PIN", 
                f"Bạn đang nhập Game PIN ({quiz_input}).\n\n"
                "⚠️ Lưu ý: PIN chỉ hoạt động khi game đang diễn ra.\n"
                "Nếu game đã kết thúc, hãy sử dụng Quiz ID thay thế.\n\n"
                "Bạn có muốn tiếp tục không?",
                icon="warning"
            )
            if not result:
                return
            
        # Clear previous results
        self.clear_results()
        
        # Start fetching in separate thread
        thread = threading.Thread(target=self.fetch_quiz_thread, args=(quiz_input,))
        thread.daemon = True
        thread.start()
        
    def run(self):
        """Start the application"""
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (self.root.winfo_width() // 2)
        y = (self.root.winfo_screenheight() // 2) - (self.root.winfo_height() // 2)
        self.root.geometry(f"+{x}+{y}")
        
        # Focus on input field
        self.quiz_input.focus()
        
        # Show startup message
        self.update_status("Sẵn sàng. Nhập Quiz ID hoặc Game PIN để bắt đầu.", "#95a5a6")
        
        # Start main loop
        self.root.mainloop()


def main():
    """Main entry point"""
    try:
        app = KahootViewer()
        app.run()
    except KeyboardInterrupt:
        print("Ứng dụng đã được đóng bởi người dùng.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Lỗi khởi tạo ứng dụng: {str(e)}")


if __name__ == "__main__":
    main()