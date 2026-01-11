import config

class GestureRecognizer:
    def __init__(self):
        # Thumb, Index, Middle, Ring, Pinky
        self.tip_ids = [4, 8, 12, 16, 20]

    def detect_gesture(self, lm_list):
        """
        Returns:
            gesture (str): MOVE, CLICK, RIGHT_CLICK, SCROLL, PAUSE, NEUTRAL
            info: None (kept lightweight for FPS)
        """

        # Safety check
        if not lm_list or len(lm_list) < 21:
            return "NEUTRAL", None

        fingers = []

        # Index, Middle, Ring, Pinky (y-axis check)
        for i in range(1, 5):
            fingers.append(
                1 if lm_list[self.tip_ids[i]][2] < lm_list[self.tip_ids[i] - 2][2] else 0
            )

        # -------- FAST PATH (NO MATH) --------

        if fingers == [1, 0, 0, 0]:
            return "MOVE", None

        if fingers == [1, 1, 0, 0]:
            return "SCROLL", None

        if fingers == [0, 0, 0, 0]:
            return "PAUSE", None

        # -------- CLICK CHECKS (MATH ONLY WHEN NEEDED) --------

        thumb_x, thumb_y = lm_list[4][1], lm_list[4][2]

        # Left Click (Thumb + Index)
        dx = lm_list[8][1] - thumb_x
        dy = lm_list[8][2] - thumb_y
        if (dx * dx + dy * dy) < (config.CLICK_DISTANCE_THRESHOLD ** 2):
            return "CLICK", None

        # Right Click (Thumb + Middle)
        dx = lm_list[12][1] - thumb_x
        dy = lm_list[12][2] - thumb_y
        if (dx * dx + dy * dy) < (config.CLICK_DISTANCE_THRESHOLD ** 2):
            return "RIGHT_CLICK", None

        return "NEUTRAL", None
