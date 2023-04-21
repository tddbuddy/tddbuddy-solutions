using System;

namespace DoorKataLib
{
    public class DoorKata
    {
        public void RunDoorKata(bool[] doors)
        {
            for (int pass = 1; pass <= doors.Length; pass++)
            {
                for (int door = pass - 1; door < doors.Length; door += pass)
                {
                    doors[door] = !doors[door];
                }
            }
        }

        public string GetDoorStateString(bool[] doors)
        {
            char[] doorChars = new char[doors.Length];
            for (int i = 0; i < doors.Length; i++)
            {
                doorChars[i] = doors[i] ? '@' : '#';
            }
            return new string(doorChars);
        }
    }
}
