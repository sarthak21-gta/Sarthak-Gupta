# Sarthak-Gupta

### What's it Do?

Basically, it's a digital notebook for keeping track of students and their rooms. After you log in (with the *super* high-tech password `1234`), you get a main menu where you can:

* **Add a New Student:** You can sign up a new student, give them an ID, and stick them in an empty room. The script's smart enough to tell you if the room's already taken or doesn't even exist.
* **Find a Student:** If you're trying to find someone, you can search for them by their ID or their name. It'll spit out all their details if it finds them.
* **Change Their Info:** Messed up a name? Need to move a student to a different room? This lets you update their record. If you move them, the script is smart enough to free up their old room.
* **Kick 'em Out (Delete):** When a student leaves, you can delete their record. This also, you guessed it, frees up their room.
* **Get Reports:** This is the "admin" part. You can:
    * See a clean list of every single student.
    * Get a report of every room and see if it's `Occupied` or `Available`.
    * Look at a "big picture" report that tells you the hostel's overall occupancy rate (%).

### How to Get it Running

This is the easy part:

1.  Make sure you have **Python 3** on your computer.
2.  Save the code as a Python file (like `hostel.py`).
3.  Open your terminal (like Command Prompt, PowerShell, or... Terminal).
4.  Go to the folder where you saved the file.
5.  Type `python "Hostel allocation assignment.py"` and hit Enter.
6.  It'll ask for the password. It's `1234`.
7.  You're in! Just type a number from the menu and press Enter.

### The (Big) Catch

**Here's the most important part:** this whole thing runs **entirely in memory**.

That means as soon as you close the program, **everything is gone.** All the students you added, all the rooms you assigned... poof! Gone. The next time you run it, it'll be back to the one example student, Sarthak.

It's great for a quick demo, but not so great for... well, running an actual hostel.

### Where to Go From Here

If you (or I) ever wanted to make this a *real* tool, the very first thing to do is add **persistence**.

That just means saving the data to a file. You could have the script dump all the student and room info into a **JSON** or **CSV** file when you exit, and then read from that file when you start it up. Or, if you're feeling fancy, you could hook it up to a real (but still simple) database like **SQLite**.

Anyway, that's pretty much it. It was a fun little project to put together!
