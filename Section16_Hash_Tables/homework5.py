import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod

class CookF(ABC):

    @abstractmethod
    def cookRule(self):
        pass


class CookFood(CookF):

    @abstractmethod
    def getCook(self):
        pass


class Dumpling(CookFood):

    def cookRule(self):
        print("Бууз хийх дүрэм:")
        print("1. Буузны гурилаа бэлдэнэ.")
        print("2. Махаа хөшиглөн амталгаагаа хийнэ.")
        print("3. Гурилаа элдээд махаа дотор нь хийж чимхэнэ.")
        print("4. Буузыг бэлэн болтол чанана.")

    def getCook(self):
        print("Бууз хийх заавар:")
        print("Усаа буцалгаад, буузаа жигнүүр дээр өрөн болтол нь 20 минут жигнэнэ.")


class Tsuivan(CookFood):

    def cookRule(self):
        print("Цуйван хийх дүрэм:")
        print("1. Гурилаа бэлэн болгож тавина.")
        print("2. Ногоотойгоо холиод махаа хуурна.")
        print("3. Дээр нь махаа давж гарахааргүй ус нэмээд гурилаа дээр нь хийнэ.")
        print("4. Усыг нь ширгэтэл болгоод сэгсэрнэ.")

    def getCook(self):
        print("Цуйван хийх заавар:")
        print("Усыг нь хийсний дараа ширгэтэл нь 10-аад минут болгоод сүүлд нь сэгсэрнэ.")


def main():
    dumpling = Dumpling()
    tsuivan = Tsuivan()

    print("\n=== Бууз хийх ===")
    dumpling.cookRule()
    dumpling.getCook()

    print("\n=== Цуйван хийх ===")
    tsuivan.cookRule()
    tsuivan.getCook()


if __name__ == "__main__":
    main()
