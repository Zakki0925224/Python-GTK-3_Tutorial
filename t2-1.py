#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python 3.6.9
# Tutorial 2.1

# GTKモジュールのインポート（GTK+3）
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# 空のウィンドウを作成
win = Gtk.Window()
# ウィンドウの削除イベントに接続して、ウィンドウを閉じるとAppが確実に終了させる
win.connect("destroy", Gtk.main_quit)
# ウィンドウの表示
win.show_all()
# ウィンドウが閉じたときに終了するGTK+処理ループ
Gtk.main()