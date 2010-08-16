gconftool-2 --set /apps/panel/toplevels/bottom_panel_screen0/auto_hide --type bool 1
gconftool-2 --set /apps/panel/toplevels/bottom_panel_screen0/expand --type bool 0
gconftool-2 --set /apps/panel/toplevels/bottom_panel_screen0/unhide_delay --type integer "1000"
gconftool-2 --set /apps/panel/toplevels/top_panel_screen0/auto_hide --type bool 1
gconftool-2 --set /apps/panel/toplevels/top_panel_screen0/expand --type bool 1
gconftool-2 --set /apps/panel/toplevels/top_panel_screen0/unhide_delay --type integer "1000"
gconftool-2 --set /apps/compiz/general/allscreens/options/close_window_key --type string "<Control><Alt>x"
gconftool-2 --set /apps/compiz/general/allscreens/options/maximize_window_key --type string ""
gconftool-2 --set /apps/compiz/general/allscreens/options/unmaximize_window_key --type string ""
gconftool-2 --set /apps/metacity/window_keybindings/toggle_fullscreen --type string "F11"
gconftool-2 --set /apps/metacity/window_keybindings/toggle_maximized --type string "<Control><Alt>f"
gconftool-2 --set /apps/metacity/window_keybindings/toggle_above --type string "<Super>t"
gconftool-2 --set --type string "/apps/compiz/plugins/extrawm/allscreens/options/toggle_always_on_top_key" --type string "<Super>t"
gconftool-2 --set /apps/metacity/window_keybindings/toggle_on_all_workspaces --type string "<Super>r"
gconftool-2 --set --type string "/apps/compiz/plugins/extrawm/allscreens/options/toggle_sticky_key" --type string "<Super>r"
gconftool-2 --set /apps/compiz/plugins/gnomecompat/allscreens/options/main_menu_key --type string ""
gconftool-2 --set /apps/metacity/global_keybindings/panel_run_dialog --type string ""
gconftool-2 --set /apps/metacity/global_keybindings/switch_to_workspace_1 --type string "<Alt>F1"
gconftool-2 --set /apps/metacity/global_keybindings/switch_to_workspace_2 --type string "<Alt>F2"
gconftool-2 --set /apps/metacity/global_keybindings/switch_to_workspace_3 --type string "<Alt>F3"
gconftool-2 --set /apps/metacity/global_keybindings/switch_to_workspace_4 --type string "<Alt>F4"
gconftool-2 --set /apps/metacity/global_keybindings/switch_to_workspace_5 --type string "<Alt>F5"
gconftool-2 --set /apps/compiz/plugins/scale/allscreens/options/initiate_key --type string "<Super>s"
# gconftool-2 --set /apps/metacity/general/theme --type string "Dust"
# gconftool-2 --set /desktop/gnome/interface/gtk_theme --type string "Dust"
gconftool-2 --set /apps/gnome-do/preferences/Do/CorePreferences/SummonKeyBinding --type string "<Alt>Escape"
gconftool-2 --set /apps/gnome-do/preferences/Do/CorePreferences/AlwaysShowResult --type bool 1
gconftool-2 --set /apps/gnome-do/preferences/Do/CorePreferences/Theme --type string "Nouveau"
gconftool-2 --set /apps/nautilus/preferences/default_folder_viewer --type string "list_view"
gconftool-2 --set /apps/nautilus/preferences/start_with_toolbar --type bool 0w
gconftool-2 --set /apps/metacity/general/focus_mode --type string "sloppy" 
gconftool-2 --set /apps/metacity/global_keybindings/run_command_1 --type string "<Super>x"
gconftool-2 --set /apps/metacity/keybinding_commands/command_1  --type string "xmms2 toggleplay"
gconftool-2 --set /apps/metacity/general/button_layout --type string "menu:minimize,maximize,close"