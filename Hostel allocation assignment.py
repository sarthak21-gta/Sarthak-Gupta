# --- HOSTEL ROOM ALLOCATION ---

# 1. Authentication Constant
PASSWORD = "1234"
MAX_TRIES = 3

# 2. Rooms Data (Dictionary: Room Number -> (Capacity, Floor) (Tuple))
ALL_ROOMS = {
    101: (2, 1),
    102: (3, 1),
    201: (2, 2),
    202: (3, 2),
    203: (4, 2),
    301: (2, 3),
    302: (5, 3)
}

# 3. Student Records (List of Dictionaries)
STUDENTS = [
    # Example student for initial testing
    {'id': 'S100', 'name': 'SARTHAK GUPTA', 'course': 'CS', 'room_number': 101}
]

# 4. Occupied Rooms (Set for fast lookup)
OCCUPIED_ROOMS = {101}


# --- HELPER FUNCTIONS ---

def display_student_details(student):
    """Formats and prints the details of a single student record."""
    print("\n--- Student Details ---")
    print(f"  ID:          {student['id']}")
    print(f"  Name:        {student['name']}")
    print(f"  Course:      {student['course']}")
    print(f"  Room Number: {student['room_number']}")

    room_num = student['room_number']
    if room_num in ALL_ROOMS:
        capacity, floor = ALL_ROOMS[room_num]
        print(f"  Floor:       {floor}")
        print(f"  Capacity:    {capacity}-bed room")
    print("-----------------------")


# --- REPORTING FUNCTIONS ---

def total_occupancy_report():
    """Calculates and displays the overall occupancy statistics."""
    total_rooms = len(ALL_ROOMS)
    occupied_rooms_count = len(OCCUPIED_ROOMS)
    available_rooms_count = total_rooms - occupied_rooms_count

    print("\n--- TOTAL OCCUPANCY REPORT ---")
    print(f"Total Rooms Available in Hostel: {total_rooms}")
    print(f"Rooms Currently Occupied:      {occupied_rooms_count}")
    print(f"Rooms Currently Available:     {available_rooms_count}")

    if total_rooms > 0:
        occupancy_rate = (occupied_rooms_count / total_rooms) * 100
        print(f"Occupancy Rate:                {occupancy_rate:.2f}%")


def student_list_report():
    """Displays a formatted list of all current student records."""
    print("\n--- STUDENT LIST REPORT ---")
    if not STUDENTS:
        print("No student records found.")
        return

    # Print header
    print(f"{'ID':<10} {'NAME':<20} {'COURSE':<10} {'ROOM':<5}")
    print("-" * 45)

    # Print each student record
    for student in STUDENTS:
        print(f"{student['id']:<10} {student['name']:<20} {student['course']:<10} {student['room_number']:<5}")


def room_availability_report():
    """Displays the status (Occupied/Available) for every room."""
    print("\n--- ROOM AVAILABILITY REPORT ---")
    print(f"{'ROOM':<8} {'CAPACITY':<10} {'FLOOR':<8} {'STATUS':<15}")
    print("-" * 41)

    for room_num, details in ALL_ROOMS.items():
        capacity, floor = details
        # Check against the SET for O(1) time complexity lookup
        status = "Occupied" if room_num in OCCUPIED_ROOMS else "Available"

        print(f"{room_num:<8} {capacity:<10} {floor:<8} {status:<15}")


def view_reports():
    """Displays a sub-menu for various hostel reports."""

    while True:
        print("\n--- REPORTS MENU ---")
        print("1. Total Occupancy Report")
        print("2. Student List Report")
        print("3. Room Availability Report")
        print("4. Back to Main Menu")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            total_occupancy_report()
        elif choice == '2':
            student_list_report()
        elif choice == '3':
            room_availability_report()
        elif choice == '4':
            break  # Exit the reports sub-menu
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# --- CORE CRUD FUNCTIONS ---

def add_student():
    """Prompts for and adds a new student record (Create)."""
    print("\n--- Add New Student ---")

    student_id = input("Enter Student ID (e.g., S101): ").strip().upper()

    if any(student['id'] == student_id for student in STUDENTS):
        print(f"❌ Error: Student with ID {student_id} already exists.")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()

    try:
        room_number = int(input("Enter Desired Room Number: "))
    except ValueError:
        print("❌ Error: Room number must be an integer.")
        return

    if room_number not in ALL_ROOMS:
        print(f"❌ Error: Room {room_number} does not exist.")
        return

    if room_number in OCCUPIED_ROOMS:
        print(f"❌ Error: Room {room_number} is already occupied.")
        return

    # Allocation successful: Update data structures
    new_student = {
        'id': student_id,
        'name': name,
        'course': course,
        'room_number': room_number
    }

    STUDENTS.append(new_student)
    OCCUPIED_ROOMS.add(room_number)

    print(f"\n✅ Success: Student {name} ({student_id}) allocated to Room {room_number}.")


def search_student():
    """Prompts for a Student ID or Name and displays the record (Read/Search)."""
    print("\n--- Search Student Record ---")
    query = input("Enter Student ID or Name to search: ").strip().lower()

    found_student = None

    for student in STUDENTS:
        if student['id'].lower() == query or student['name'].lower() == query:
            found_student = student
            break

    if found_student:
        display_student_details(found_student)
        return found_student
    else:
        print(f"\n❌ Error: No student found matching '{query}'.")
        return None


def delete_student():
    """Finds a student by ID and removes their record, freeing up the room (Delete)."""
    print("\n--- Delete Student Record ---")

    student_id = input("Enter Student ID to delete: ").strip().upper()

    student_index = -1
    room_to_free = None

    for index, student in enumerate(STUDENTS):
        if student['id'] == student_id:
            student_index = index
            room_to_free = student['room_number']
            break

    if student_index != -1:
        # 1. Remove the student dictionary from the STUDENTS list
        deleted_student = STUDENTS.pop(student_index)

        # 2. Remove the room number from the OCCUPIED_ROOMS set (free the room)
        if room_to_free in OCCUPIED_ROOMS:
            OCCUPIED_ROOMS.remove(room_to_free)

        print(f"\n✅ Success: Record for {deleted_student['name']} (ID: {student_id}) deleted.")
        print(f"Room {room_to_free} is now available.")
    else:
        print(f"\n❌ Error: No student found with ID '{student_id}'. Deletion failed.")


def modify_student():
    """Allows the administrator to modify a student's name, course, or room (Update)."""
    print("\n--- Modify Student Record ---")

    student_id = input("Enter the ID of the student to modify: ").strip().upper()

    student_to_modify = None
    student_index = -1
    for index, student in enumerate(STUDENTS):
        if student['id'] == student_id:
            student_to_modify = student
            student_index = index
            break

    if not student_to_modify:
        print(f"❌ Error: No student found with ID '{student_id}'.")
        return

    display_student_details(student_to_modify)

    print("\nWhat detail would you like to change?")
    print("1. Name")
    print("2. Course")
    print("3. Room Number")
    choice = input("Enter choice (1-3) or press Enter to cancel: ").strip()

    if choice == '1':
        new_name = input(f"Enter new Name (current: {student_to_modify['name']}): ").strip()
        STUDENTS[student_index]['name'] = new_name
        print(f"\n✅ Success: Student Name updated to {new_name}.")

    elif choice == '2':
        new_course = input(f"Enter new Course (current: {student_to_modify['course']}): ").strip()
        STUDENTS[student_index]['course'] = new_course
        print(f"\n✅ Success: Student Course updated to {new_course}.")

    elif choice == '3':
        try:
            new_room = int(input(f"Enter new Room Number (current: {student_to_modify['room_number']}): "))
        except ValueError:
            print("❌ Error: Room number must be an integer. Modification cancelled.")
            return

        if new_room not in ALL_ROOMS:
            print(f"❌ Error: Room {new_room} does not exist. Modification cancelled.")
            return
        if new_room in OCCUPIED_ROOMS and new_room != student_to_modify['room_number']:
            print(f"❌ Error: Room {new_room} is already occupied. Modification cancelled.")
            return

        # Room Swap Logic
        old_room = student_to_modify['room_number']

        STUDENTS[student_index]['room_number'] = new_room

        if old_room in OCCUPIED_ROOMS:
            OCCUPIED_ROOMS.remove(old_room)  # Free up the old room
        OCCUPIED_ROOMS.add(new_room)  # Occupy the new room

        print(f"\n✅ Success: Room reassigned from {old_room} to {new_room}.")

    else:
        print("Modification cancelled.")


# --- AUTHENTICATION & MAIN PROGRAM FLOW ---

def authenticate():
    """Handles the admin login with a limited number of attempts."""
    for attempt in range(1, MAX_TRIES + 1):
        user_input = input(f"Enter Administrator Password (Attempt {attempt}/{MAX_TRIES}): ")

        if user_input == PASSWORD:
            print("\nLogin Successful! Welcome, Administrator.")
            return True
        else:
            print("Invalid Password.")

    print("\nAccess Denied. Too many failed attempts.")
    return False


def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n--- Main Menu ---")
        print("1. Add a new student record")
        print("2. Modify a student's room or details")
        print("3. Delete a student's record")
        print("4. Search for a student")
        print("5. View reports")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            modify_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            view_reports()
        elif choice == '6':
            print("Exiting Hostel Allocation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# --- Program Entry Point ---
if __name__ == "__main__":
    print("Welcome to Hostel Room Allocation System")
    if authenticate():
        main_menu()