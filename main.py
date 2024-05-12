"""main"""
import tkinter as tk


def main():
    """メイン関数"""
    # メインウィンドウを作成
    root = tk.Tk()
    root.title("simple desktop app title")

    # ラベルウィジェットを作成して配置
    label = tk.Label(root, text="HELLO WORLD", font=("Arial", 24))
    label.pack(expand=True)

    # GUIを開始
    root.mainloop()

if __name__ == "__main__":
    main()
