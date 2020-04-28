#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python 3.6.9
# Tutorial 2.2

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Gtk.Windowと独自のMyWindowクラスを定義するためのサブクラス化
class MyWindow(Gtk.Window):
    def __init__(self):
        # スーパークラスのコンンストラクターを呼び出す
        # プロパティ・タイトルをHello Worldに設定
        Gtk.Window.__init__(self, title = "Hello World")

        # ボタンウィジットの作成
        self.button = Gtk.Button(label = "Hello World")
        # クリック時の処理を接続
        self.button.connect("clicked", self.on_button_clicked)
        # トップレベルウィンドウの子として追加
        self.add(self.button)

    # ボタンクリック時の処理メソッド
    def on_button_clicked(self, widget):
        print("Hello World")

# MyWindowのインスタンスを作成
win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()