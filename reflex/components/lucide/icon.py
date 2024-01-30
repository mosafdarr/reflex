"""Lucide Icon component."""

from reflex.components.component import Component
from reflex.style import Style
from reflex.utils import format
from reflex.vars import Var


class LucideIconComponent(Component):
    """Lucide Icon Component."""

    library = "lucide-react@0.314.0"


class Icon(LucideIconComponent):
    """An Icon component."""

    tag = "None"

    # The size of the icon in pixels.
    size: Var[int]

    @classmethod
    def create(cls, *children, **props) -> Component:
        """Initialize the Icon component.

        Run some additional checks on Icon component.

        Args:
            *children: The positional arguments
            **props: The keyword arguments

        Raises:
            AttributeError: The errors tied to bad usage of the Icon component.
            ValueError: If the icon tag is invalid.

        Returns:
            The created component.
        """
        if children:
            if len(children) == 1 and type(children[0]) == str:
                props["tag"] = children[0]
            else:
                raise AttributeError(
                    f"Passing multiple children to Icon component is not allowed: remove positional arguments {children[1:]} to fix"
                )
        if "tag" not in props.keys():
            raise AttributeError("Missing 'tag' keyword-argument for Icon")

        if (
            type(props["tag"]) != str
            or format.to_snake_case(props["tag"]) not in LUCIDE_ICON_LIST
        ):
            raise ValueError(
                f"Invalid icon tag: {props['tag']}. Please use one of the following: {', '.join(LUCIDE_ICON_LIST[0:25])}, ..."
                "\nSee full list at https://lucide.dev/icons."
            )

        props["tag"] = format.to_title_case(format.to_snake_case(props["tag"])) + "Icon"
        props["alias"] = f"Lucide{props['tag']}"
        return super().create(*children, **props)

    def _apply_theme(self, theme: Component | None):
        self.style = Style(
            {
                "color": f"var(--current-color)",
                **self.style,
            }
        )


LUCIDE_ICON_LIST = [
    "a_arrow_down",
    "a_arrow_up",
    "a_large_small",
    "accessibility",
    "activity",
    "activity_square",
    "air_vent",
    "airplay",
    "alarm_clock",
    "alarm_clock_check",
    "alarm_clock_minus",
    "alarm_clock_off",
    "alarm_clock_plus",
    "alarm_smoke",
    "album",
    "alert_circle",
    "alert_octagon",
    "alert_triangle",
    "align_center",
    "align_center_horizontal",
    "align_center_vertical",
    "align_end_horizontal",
    "align_end_vertical",
    "align_horizontal_distribute_center",
    "align_horizontal_distribute_end",
    "align_horizontal_distribute_start",
    "align_horizontal_justify_center",
    "align_horizontal_justify_end",
    "align_horizontal_justify_start",
    "align_horizontal_space_around",
    "align_horizontal_space_between",
    "align_justify",
    "align_left",
    "align_right",
    "align_start_horizontal",
    "align_start_vertical",
    "align_vertical_distribute_center",
    "align_vertical_distribute_end",
    "align_vertical_distribute_start",
    "align_vertical_justify_center",
    "align_vertical_justify_end",
    "align_vertical_justify_start",
    "align_vertical_space_around",
    "align_vertical_space_between",
    "ampersand",
    "ampersands",
    "anchor",
    "angry",
    "annoyed",
    "antenna",
    "anvil",
    "aperture",
    "app_window",
    "apple",
    "archive",
    "archive_restore",
    "archive_x",
    "area_chart",
    "armchair",
    "arrow_big_down",
    "arrow_big_down_dash",
    "arrow_big_left",
    "arrow_big_left_dash",
    "arrow_big_right",
    "arrow_big_right_dash",
    "arrow_big_up",
    "arrow_big_up_dash",
    "arrow_down",
    "arrow_down_0_1",
    "arrow_down_1_0",
    "arrow_down_a_z",
    "arrow_down_circle",
    "arrow_down_from_line",
    "arrow_down_left",
    "arrow_down_left_from_circle",
    "arrow_down_left_from_square",
    "arrow_down_left_square",
    "arrow_down_narrow_wide",
    "arrow_down_right",
    "arrow_down_right_from_circle",
    "arrow_down_right_from_square",
    "arrow_down_right_square",
    "arrow_down_square",
    "arrow_down_to_dot",
    "arrow_down_to_line",
    "arrow_down_up",
    "arrow_down_wide_narrow",
    "arrow_down_z_a",
    "arrow_left",
    "arrow_left_circle",
    "arrow_left_from_line",
    "arrow_left_right",
    "arrow_left_square",
    "arrow_left_to_line",
    "arrow_right",
    "arrow_right_circle",
    "arrow_right_from_line",
    "arrow_right_left",
    "arrow_right_square",
    "arrow_right_to_line",
    "arrow_up",
    "arrow_up_0_1",
    "arrow_up_1_0",
    "arrow_up_a_z",
    "arrow_up_circle",
    "arrow_up_down",
    "arrow_up_from_dot",
    "arrow_up_from_line",
    "arrow_up_left",
    "arrow_up_left_from_circle",
    "arrow_up_left_from_square",
    "arrow_up_left_square",
    "arrow_up_narrow_wide",
    "arrow_up_right",
    "arrow_up_right_from_circle",
    "arrow_up_right_from_square",
    "arrow_up_right_square",
    "arrow_up_square",
    "arrow_up_to_line",
    "arrow_up_wide_narrow",
    "arrow_up_z_a",
    "arrows_up_from_line",
    "asterisk",
    "asterisk_square",
    "at_sign",
    "atom",
    "audio_lines",
    "audio_waveform",
    "award",
    "axe",
    "axis_3d",
    "baby",
    "backpack",
    "badge",
    "badge_alert",
    "badge_cent",
    "badge_check",
    "badge_dollar_sign",
    "badge_euro",
    "badge_help",
    "badge_indian_rupee",
    "badge_info",
    "badge_japanese_yen",
    "badge_minus",
    "badge_percent",
    "badge_plus",
    "badge_pound_sterling",
    "badge_russian_ruble",
    "badge_swiss_franc",
    "badge_x",
    "baggage_claim",
    "ban",
    "banana",
    "banknote",
    "bar_chart",
    "bar_chart_2",
    "bar_chart_3",
    "bar_chart_4",
    "bar_chart_big",
    "bar_chart_horizontal",
    "bar_chart_horizontal_big",
    "barcode",
    "baseline",
    "bath",
    "battery",
    "battery_charging",
    "battery_full",
    "battery_low",
    "battery_medium",
    "battery_warning",
    "beaker",
    "bean",
    "bean_off",
    "bed",
    "bed_double",
    "bed_single",
    "beef",
    "beer",
    "bell",
    "bell_dot",
    "bell_electric",
    "bell_minus",
    "bell_off",
    "bell_plus",
    "bell_ring",
    "between_horizontal_end",
    "between_horizontal_start",
    "between_vertical_end",
    "between_vertical_start",
    "bike",
    "binary",
    "biohazard",
    "bird",
    "bitcoin",
    "blend",
    "blinds",
    "blocks",
    "bluetooth",
    "bluetooth_connected",
    "bluetooth_off",
    "bluetooth_searching",
    "bold",
    "bolt",
    "bomb",
    "bone",
    "book",
    "book_a",
    "book_audio",
    "book_check",
    "book_copy",
    "book_dashed",
    "book_down",
    "book_headphones",
    "book_heart",
    "book_image",
    "book_key",
    "book_lock",
    "book_marked",
    "book_minus",
    "book_open",
    "book_open_check",
    "book_open_text",
    "book_plus",
    "book_text",
    "book_type",
    "book_up",
    "book_up_2",
    "book_user",
    "book_x",
    "bookmark",
    "bookmark_check",
    "bookmark_minus",
    "bookmark_plus",
    "bookmark_x",
    "boom_box",
    "bot",
    "box",
    "box_select",
    "boxes",
    "braces",
    "brackets",
    "brain",
    "brain_circuit",
    "brain_cog",
    "brick_wall",
    "briefcase",
    "bring_to_front",
    "brush",
    "bug",
    "bug_off",
    "bug_play",
    "building",
    "building_2",
    "bus",
    "bus_front",
    "cable",
    "cable_car",
    "cake",
    "cake_slice",
    "calculator",
    "calendar",
    "calendar_check",
    "calendar_check_2",
    "calendar_clock",
    "calendar_days",
    "calendar_fold",
    "calendar_heart",
    "calendar_minus",
    "calendar_minus_2",
    "calendar_off",
    "calendar_plus",
    "calendar_plus_2",
    "calendar_range",
    "calendar_search",
    "calendar_x",
    "calendar_x_2",
    "camera",
    "camera_off",
    "candlestick_chart",
    "candy",
    "candy_cane",
    "candy_off",
    "car",
    "car_front",
    "car_taxi_front",
    "caravan",
    "carrot",
    "case_lower",
    "case_sensitive",
    "case_upper",
    "cassette_tape",
    "cast",
    "castle",
    "cat",
    "cctv",
    "check",
    "check_check",
    "check_circle",
    "check_circle_2",
    "check_square",
    "check_square_2",
    "chef_hat",
    "cherry",
    "chevron_down",
    "chevron_down_circle",
    "chevron_down_square",
    "chevron_first",
    "chevron_last",
    "chevron_left",
    "chevron_left_circle",
    "chevron_left_square",
    "chevron_right",
    "chevron_right_circle",
    "chevron_right_square",
    "chevron_up",
    "chevron_up_circle",
    "chevron_up_square",
    "chevrons_down",
    "chevrons_down_up",
    "chevrons_left",
    "chevrons_left_right",
    "chevrons_right",
    "chevrons_right_left",
    "chevrons_up",
    "chevrons_up_down",
    "chrome",
    "church",
    "cigarette",
    "cigarette_off",
    "circle",
    "circle_dashed",
    "circle_dollar_sign",
    "circle_dot",
    "circle_dot_dashed",
    "circle_ellipsis",
    "circle_equal",
    "circle_off",
    "circle_slash",
    "circle_slash_2",
    "circle_user",
    "circle_user_round",
    "circuit_board",
    "citrus",
    "clapperboard",
    "clipboard",
    "clipboard_check",
    "clipboard_copy",
    "clipboard_list",
    "clipboard_paste",
    "clipboard_pen",
    "clipboard_pen_line",
    "clipboard_type",
    "clipboard_x",
    "clock",
    "clock_1",
    "clock_10",
    "clock_11",
    "clock_12",
    "clock_2",
    "clock_3",
    "clock_4",
    "clock_5",
    "clock_6",
    "clock_7",
    "clock_8",
    "clock_9",
    "cloud",
    "cloud_cog",
    "cloud_drizzle",
    "cloud_fog",
    "cloud_hail",
    "cloud_lightning",
    "cloud_moon",
    "cloud_moon_rain",
    "cloud_off",
    "cloud_rain",
    "cloud_rain_wind",
    "cloud_snow",
    "cloud_sun",
    "cloud_sun_rain",
    "cloudy",
    "clover",
    "club",
    "code",
    "code_2",
    "code_square",
    "codepen",
    "codesandbox",
    "coffee",
    "cog",
    "coins",
    "columns_2",
    "columns_3",
    "columns_4",
    "combine",
    "command",
    "compass",
    "component",
    "computer",
    "concierge_bell",
    "cone",
    "construction",
    "contact",
    "contact_2",
    "container",
    "contrast",
    "cookie",
    "cooking_pot",
    "copy",
    "copy_check",
    "copy_minus",
    "copy_plus",
    "copy_slash",
    "copy_x",
    "copyleft",
    "copyright",
    "corner_down_left",
    "corner_down_right",
    "corner_left_down",
    "corner_left_up",
    "corner_right_down",
    "corner_right_up",
    "corner_up_left",
    "corner_up_right",
    "cpu",
    "creative_commons",
    "credit_card",
    "croissant",
    "crop",
    "cross",
    "crosshair",
    "crown",
    "cuboid",
    "cup_soda",
    "currency",
    "cylinder",
    "database",
    "database_backup",
    "database_zap",
    "delete",
    "dessert",
    "diameter",
    "diamond",
    "dice_1",
    "dice_2",
    "dice_3",
    "dice_4",
    "dice_5",
    "dice_6",
    "dices",
    "diff",
    "disc",
    "disc_2",
    "disc_3",
    "disc_album",
    "divide",
    "divide_circle",
    "divide_square",
    "dna",
    "dna_off",
    "dog",
    "dollar_sign",
    "donut",
    "door_closed",
    "door_open",
    "dot",
    "dot_square",
    "download",
    "download_cloud",
    "drafting_compass",
    "drama",
    "dribbble",
    "drill",
    "droplet",
    "droplets",
    "drum",
    "drumstick",
    "dumbbell",
    "ear",
    "ear_off",
    "eclipse",
    "egg",
    "egg_fried",
    "egg_off",
    "equal",
    "equal_not",
    "equal_square",
    "eraser",
    "euro",
    "expand",
    "external_link",
    "eye",
    "eye_off",
    "facebook",
    "factory",
    "fan",
    "fast_forward",
    "feather",
    "fence",
    "ferris_wheel",
    "figma",
    "file",
    "file_archive",
    "file_audio",
    "file_audio_2",
    "file_axis_3d",
    "file_badge",
    "file_badge_2",
    "file_bar_chart",
    "file_bar_chart_2",
    "file_box",
    "file_check",
    "file_check_2",
    "file_clock",
    "file_code",
    "file_code_2",
    "file_cog",
    "file_diff",
    "file_digit",
    "file_down",
    "file_heart",
    "file_image",
    "file_input",
    "file_json",
    "file_json_2",
    "file_key",
    "file_key_2",
    "file_line_chart",
    "file_lock",
    "file_lock_2",
    "file_minus",
    "file_minus_2",
    "file_music",
    "file_output",
    "file_pen",
    "file_pen_line",
    "file_pie_chart",
    "file_plus",
    "file_plus_2",
    "file_question",
    "file_scan",
    "file_search",
    "file_search_2",
    "file_sliders",
    "file_spreadsheet",
    "file_stack",
    "file_symlink",
    "file_terminal",
    "file_text",
    "file_type",
    "file_type_2",
    "file_up",
    "file_video",
    "file_video_2",
    "file_volume",
    "file_volume_2",
    "file_warning",
    "file_x",
    "file_x_2",
    "files",
    "film",
    "filter",
    "filter_x",
    "fingerprint",
    "fire_extinguisher",
    "fish",
    "fish_off",
    "fish_symbol",
    "flag",
    "flag_off",
    "flag_triangle_left",
    "flag_triangle_right",
    "flame",
    "flame_kindling",
    "flashlight",
    "flashlight_off",
    "flask_conical",
    "flask_conical_off",
    "flask_round",
    "flip_horizontal",
    "flip_horizontal_2",
    "flip_vertical",
    "flip_vertical_2",
    "flower",
    "flower_2",
    "focus",
    "fold_horizontal",
    "fold_vertical",
    "folder",
    "folder_archive",
    "folder_check",
    "folder_clock",
    "folder_closed",
    "folder_cog",
    "folder_dot",
    "folder_down",
    "folder_git",
    "folder_git_2",
    "folder_heart",
    "folder_input",
    "folder_kanban",
    "folder_key",
    "folder_lock",
    "folder_minus",
    "folder_open",
    "folder_open_dot",
    "folder_output",
    "folder_pen",
    "folder_plus",
    "folder_root",
    "folder_search",
    "folder_search_2",
    "folder_symlink",
    "folder_sync",
    "folder_tree",
    "folder_up",
    "folder_x",
    "folders",
    "footprints",
    "forklift",
    "form_input",
    "forward",
    "frame",
    "framer",
    "frown",
    "fuel",
    "fullscreen",
    "function_square",
    "gallery_horizontal",
    "gallery_horizontal_end",
    "gallery_thumbnails",
    "gallery_vertical",
    "gallery_vertical_end",
    "gamepad",
    "gamepad_2",
    "gantt_chart",
    "gantt_chart_square",
    "gauge",
    "gauge_circle",
    "gavel",
    "gem",
    "ghost",
    "gift",
    "git_branch",
    "git_branch_plus",
    "git_commit_horizontal",
    "git_commit_vertical",
    "git_compare",
    "git_compare_arrows",
    "git_fork",
    "git_graph",
    "git_merge",
    "git_pull_request",
    "git_pull_request_arrow",
    "git_pull_request_closed",
    "git_pull_request_create",
    "git_pull_request_create_arrow",
    "git_pull_request_draft",
    "github",
    "gitlab",
    "glass_water",
    "glasses",
    "globe",
    "globe_2",
    "goal",
    "grab",
    "graduation_cap",
    "grape",
    "grid_2x2",
    "grid_3x3",
    "grip",
    "grip_horizontal",
    "grip_vertical",
    "group",
    "guitar",
    "hammer",
    "hand",
    "hand_metal",
    "hard_drive",
    "hard_drive_download",
    "hard_drive_upload",
    "hard_hat",
    "hash",
    "haze",
    "hdmi_port",
    "heading",
    "heading_1",
    "heading_2",
    "heading_3",
    "heading_4",
    "heading_5",
    "heading_6",
    "headphones",
    "heart",
    "heart_crack",
    "heart_handshake",
    "heart_off",
    "heart_pulse",
    "heater",
    "help_circle",
    "helping_hand",
    "hexagon",
    "highlighter",
    "history",
    "home",
    "hop",
    "hop_off",
    "hotel",
    "hourglass",
    "ice_cream",
    "ice_cream_2",
    "image",
    "image_down",
    "image_minus",
    "image_off",
    "image_plus",
    "import",
    "inbox",
    "indent",
    "indian_rupee",
    "infinity",
    "info",
    "inspection_panel",
    "instagram",
    "italic",
    "iteration_ccw",
    "iteration_cw",
    "japanese_yen",
    "joystick",
    "kanban",
    "kanban_square",
    "kanban_square_dashed",
    "key",
    "key_round",
    "key_square",
    "keyboard",
    "keyboard_music",
    "lamp",
    "lamp_ceiling",
    "lamp_desk",
    "lamp_floor",
    "lamp_wall_down",
    "lamp_wall_up",
    "land_plot",
    "landmark",
    "languages",
    "laptop",
    "laptop_2",
    "lasso",
    "lasso_select",
    "laugh",
    "layers",
    "layers_2",
    "layers_3",
    "layout_dashboard",
    "layout_grid",
    "layout_list",
    "layout_panel_left",
    "layout_panel_top",
    "layout_template",
    "leaf",
    "leafy_green",
    "library",
    "library_big",
    "library_square",
    "life_buoy",
    "ligature",
    "lightbulb",
    "lightbulb_off",
    "line_chart",
    "link",
    "link_2",
    "link_2_off",
    "linkedin",
    "list",
    "list_checks",
    "list_collapse",
    "list_end",
    "list_filter",
    "list_minus",
    "list_music",
    "list_ordered",
    "list_plus",
    "list_restart",
    "list_start",
    "list_todo",
    "list_tree",
    "list_video",
    "list_x",
    "loader",
    "loader_2",
    "locate",
    "locate_fixed",
    "locate_off",
    "lock",
    "lock_keyhole",
    "log_in",
    "log_out",
    "lollipop",
    "luggage",
    "m_square",
    "magnet",
    "mail",
    "mail_check",
    "mail_minus",
    "mail_open",
    "mail_plus",
    "mail_question",
    "mail_search",
    "mail_warning",
    "mail_x",
    "mailbox",
    "mails",
    "map",
    "map_pin",
    "map_pin_off",
    "map_pinned",
    "martini",
    "maximize",
    "maximize_2",
    "medal",
    "megaphone",
    "megaphone_off",
    "meh",
    "memory_stick",
    "menu",
    "menu_square",
    "merge",
    "message_circle",
    "message_circle_code",
    "message_circle_dashed",
    "message_circle_heart",
    "message_circle_more",
    "message_circle_off",
    "message_circle_plus",
    "message_circle_question",
    "message_circle_reply",
    "message_circle_warning",
    "message_circle_x",
    "message_square",
    "message_square_code",
    "message_square_dashed",
    "message_square_diff",
    "message_square_dot",
    "message_square_heart",
    "message_square_more",
    "message_square_off",
    "message_square_plus",
    "message_square_quote",
    "message_square_reply",
    "message_square_share",
    "message_square_text",
    "message_square_warning",
    "message_square_x",
    "messages_square",
    "mic",
    "mic_2",
    "mic_off",
    "microscope",
    "microwave",
    "milestone",
    "milk",
    "milk_off",
    "minimize",
    "minimize_2",
    "minus",
    "minus_circle",
    "minus_square",
    "monitor",
    "monitor_check",
    "monitor_dot",
    "monitor_down",
    "monitor_off",
    "monitor_pause",
    "monitor_play",
    "monitor_smartphone",
    "monitor_speaker",
    "monitor_stop",
    "monitor_up",
    "monitor_x",
    "moon",
    "moon_star",
    "more_horizontal",
    "more_vertical",
    "mountain",
    "mountain_snow",
    "mouse",
    "mouse_pointer",
    "mouse_pointer_2",
    "mouse_pointer_click",
    "mouse_pointer_square",
    "mouse_pointer_square_dashed",
    "move",
    "move_3d",
    "move_diagonal",
    "move_diagonal_2",
    "move_down",
    "move_down_left",
    "move_down_right",
    "move_horizontal",
    "move_left",
    "move_right",
    "move_up",
    "move_up_left",
    "move_up_right",
    "move_vertical",
    "music",
    "music_2",
    "music_3",
    "music_4",
    "navigation",
    "navigation_2",
    "navigation_2_off",
    "navigation_off",
    "network",
    "newspaper",
    "nfc",
    "notebook",
    "notebook_pen",
    "notebook_tabs",
    "notebook_text",
    "notepad_text",
    "notepad_text_dashed",
    "nut",
    "nut_off",
    "octagon",
    "option",
    "orbit",
    "outdent",
    "package",
    "package_2",
    "package_check",
    "package_minus",
    "package_open",
    "package_plus",
    "package_search",
    "package_x",
    "paint_bucket",
    "paint_roller",
    "paintbrush",
    "paintbrush_2",
    "palette",
    "palmtree",
    "panel_bottom",
    "panel_bottom_close",
    "panel_bottom_dashed",
    "panel_bottom_open",
    "panel_left",
    "panel_left_close",
    "panel_left_dashed",
    "panel_left_open",
    "panel_right",
    "panel_right_close",
    "panel_right_dashed",
    "panel_right_open",
    "panel_top",
    "panel_top_close",
    "panel_top_dashed",
    "panel_top_open",
    "panels_left_bottom",
    "panels_right_bottom",
    "panels_top_left",
    "paperclip",
    "parentheses",
    "parking_circle",
    "parking_circle_off",
    "parking_meter",
    "parking_square",
    "parking_square_off",
    "party_popper",
    "pause",
    "pause_circle",
    "pause_octagon",
    "paw_print",
    "pc_case",
    "pen",
    "pen_line",
    "pen_tool",
    "pencil",
    "pencil_line",
    "pencil_ruler",
    "pentagon",
    "percent",
    "percent_circle",
    "percent_diamond",
    "percent_square",
    "person_standing",
    "phone",
    "phone_call",
    "phone_forwarded",
    "phone_incoming",
    "phone_missed",
    "phone_off",
    "phone_outgoing",
    "pi",
    "pi_square",
    "piano",
    "picture_in_picture",
    "picture_in_picture_2",
    "pie_chart",
    "piggy_bank",
    "pilcrow",
    "pilcrow_square",
    "pill",
    "pin",
    "pin_off",
    "pipette",
    "pizza",
    "plane",
    "plane_landing",
    "plane_takeoff",
    "play",
    "play_circle",
    "play_square",
    "plug",
    "plug_2",
    "plug_zap",
    "plug_zap_2",
    "plus",
    "plus_circle",
    "plus_square",
    "pocket",
    "pocket_knife",
    "podcast",
    "pointer",
    "pointer_off",
    "popcorn",
    "popsicle",
    "pound_sterling",
    "power",
    "power_circle",
    "power_off",
    "power_square",
    "presentation",
    "printer",
    "projector",
    "puzzle",
    "pyramid",
    "qr_code",
    "quote",
    "rabbit",
    "radar",
    "radiation",
    "radio",
    "radio_receiver",
    "radio_tower",
    "radius",
    "rail_symbol",
    "rainbow",
    "rat",
    "ratio",
    "receipt",
    "receipt_cent",
    "receipt_euro",
    "receipt_indian_rupee",
    "receipt_japanese_yen",
    "receipt_pound_sterling",
    "receipt_russian_ruble",
    "receipt_swiss_franc",
    "receipt_text",
    "rectangle_horizontal",
    "rectangle_vertical",
    "recycle",
    "redo",
    "redo_2",
    "redo_dot",
    "refresh_ccw",
    "refresh_ccw_dot",
    "refresh_cw",
    "refresh_cw_off",
    "refrigerator",
    "regex",
    "remove_formatting",
    "repeat",
    "repeat_1",
    "repeat_2",
    "replace",
    "replace_all",
    "reply",
    "reply_all",
    "rewind",
    "ribbon",
    "rocket",
    "rocking_chair",
    "roller_coaster",
    "rotate_3d",
    "rotate_ccw",
    "rotate_cw",
    "route",
    "route_off",
    "router",
    "rows_2",
    "rows_3",
    "rows_4",
    "rss",
    "ruler",
    "russian_ruble",
    "sailboat",
    "salad",
    "sandwich",
    "satellite",
    "satellite_dish",
    "save",
    "save_all",
    "scale",
    "scale_3d",
    "scaling",
    "scan",
    "scan_barcode",
    "scan_eye",
    "scan_face",
    "scan_line",
    "scan_search",
    "scan_text",
    "scatter_chart",
    "school",
    "school_2",
    "scissors",
    "scissors_line_dashed",
    "scissors_square",
    "scissors_square_dashed_bottom",
    "screen_share",
    "screen_share_off",
    "scroll",
    "scroll_text",
    "search",
    "search_check",
    "search_code",
    "search_slash",
    "search_x",
    "send",
    "send_horizontal",
    "send_to_back",
    "separator_horizontal",
    "separator_vertical",
    "server",
    "server_cog",
    "server_crash",
    "server_off",
    "settings",
    "settings_2",
    "shapes",
    "share",
    "share_2",
    "sheet",
    "shell",
    "shield",
    "shield_alert",
    "shield_ban",
    "shield_check",
    "shield_ellipsis",
    "shield_half",
    "shield_minus",
    "shield_off",
    "shield_plus",
    "shield_question",
    "shield_x",
    "ship",
    "ship_wheel",
    "shirt",
    "shopping_bag",
    "shopping_basket",
    "shopping_cart",
    "shovel",
    "shower_head",
    "shrink",
    "shrub",
    "shuffle",
    "sigma",
    "sigma_square",
    "signal",
    "signal_high",
    "signal_low",
    "signal_medium",
    "signal_zero",
    "signpost",
    "signpost_big",
    "siren",
    "skip_back",
    "skip_forward",
    "skull",
    "slack",
    "slash",
    "slash_square",
    "slice",
    "sliders",
    "sliders_horizontal",
    "smartphone",
    "smartphone_charging",
    "smartphone_nfc",
    "smile",
    "smile_plus",
    "snail",
    "snowflake",
    "sofa",
    "soup",
    "space",
    "spade",
    "sparkle",
    "sparkles",
    "speaker",
    "speech",
    "spell_check",
    "spell_check_2",
    "spline",
    "split",
    "split_square_horizontal",
    "split_square_vertical",
    "spray_can",
    "sprout",
    "square",
    "square_dashed_bottom",
    "square_dashed_bottom_code",
    "square_pen",
    "square_stack",
    "square_user",
    "square_user_round",
    "squircle",
    "squirrel",
    "stamp",
    "star",
    "star_half",
    "star_off",
    "step_back",
    "step_forward",
    "stethoscope",
    "sticker",
    "sticky_note",
    "stop_circle",
    "store",
    "stretch_horizontal",
    "stretch_vertical",
    "strikethrough",
    "subscript",
    "subtitles",
    "sun",
    "sun_dim",
    "sun_medium",
    "sun_moon",
    "sun_snow",
    "sunrise",
    "sunset",
    "superscript",
    "swatch_book",
    "swiss_franc",
    "switch_camera",
    "sword",
    "swords",
    "syringe",
    "table",
    "table_2",
    "table_properties",
    "tablet",
    "tablet_smartphone",
    "tablets",
    "tag",
    "tags",
    "tally_1",
    "tally_2",
    "tally_3",
    "tally_4",
    "tally_5",
    "tangent",
    "target",
    "tent",
    "tent_tree",
    "terminal",
    "terminal_square",
    "test_tube",
    "test_tube_2",
    "test_tubes",
    "text",
    "text_cursor",
    "text_cursor_input",
    "text_quote",
    "text_search",
    "text_select",
    "theater",
    "thermometer",
    "thermometer_snowflake",
    "thermometer_sun",
    "thumbs_down",
    "thumbs_up",
    "ticket",
    "ticket_check",
    "ticket_minus",
    "ticket_percent",
    "ticket_plus",
    "ticket_slash",
    "ticket_x",
    "timer",
    "timer_off",
    "timer_reset",
    "toggle_left",
    "toggle_right",
    "tornado",
    "torus",
    "touchpad",
    "touchpad_off",
    "tower_control",
    "toy_brick",
    "tractor",
    "traffic_cone",
    "train_front",
    "train_front_tunnel",
    "train_track",
    "tram_front",
    "trash",
    "trash_2",
    "tree_deciduous",
    "tree_pine",
    "trees",
    "trello",
    "trending_down",
    "trending_up",
    "triangle",
    "triangle_right",
    "trophy",
    "truck",
    "turtle",
    "tv",
    "tv_2",
    "twitch",
    "twitter",
    "type",
    "umbrella",
    "umbrella_off",
    "underline",
    "undo",
    "undo_2",
    "undo_dot",
    "unfold_horizontal",
    "unfold_vertical",
    "ungroup",
    "unlink",
    "unlink_2",
    "unlock",
    "unlock_keyhole",
    "unplug",
    "upload",
    "upload_cloud",
    "usb",
    "user",
    "user_check",
    "user_cog",
    "user_minus",
    "user_plus",
    "user_round",
    "user_round_check",
    "user_round_cog",
    "user_round_minus",
    "user_round_plus",
    "user_round_search",
    "user_round_x",
    "user_search",
    "user_x",
    "users",
    "users_round",
    "utensils",
    "utensils_crossed",
    "utility_pole",
    "variable",
    "vault",
    "vegan",
    "venetian_mask",
    "vibrate",
    "vibrate_off",
    "video",
    "video_off",
    "videotape",
    "view",
    "voicemail",
    "volume",
    "volume_1",
    "volume_2",
    "volume_x",
    "vote",
    "wallet",
    "wallet_2",
    "wallet_cards",
    "wallpaper",
    "wand",
    "wand_2",
    "warehouse",
    "washing_machine",
    "watch",
    "waves",
    "waypoints",
    "webcam",
    "webhook",
    "weight",
    "wheat",
    "wheat_off",
    "whole_word",
    "wifi",
    "wifi_off",
    "wind",
    "wine",
    "wine_off",
    "workflow",
    "wrap_text",
    "wrench",
    "x",
    "x_circle",
    "x_octagon",
    "x_square",
    "youtube",
    "zap",
    "zap_off",
    "zoom_in",
    "zoom_out",
]
