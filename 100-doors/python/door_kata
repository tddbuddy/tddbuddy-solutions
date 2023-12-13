class DoorKata:
    def run_door_kata(self, doors):
        for pass_num in range(1, len(doors) + 1):
            for door in range(pass_num - 1, len(doors), pass_num):
                doors[door] = not doors[door]

    def get_door_state_string(self, doors):
        return ''.join('@' if door else '#' for door in doors)

