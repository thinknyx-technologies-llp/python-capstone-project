employees = []
while True:
    print("\nEmployee Management")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Remove Employee")
    print("4. Update Employee")
    print("5. Search for Employees")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        empno = int(input("Enter Employee Number: "))
        empname = input("Enter Employee Name: ")
        designation = input("Enter Designation: ")
        employees.append({'empno': empno, 'empname': empname, 'designation': designation})
        print(f"Employee with empno: {empno} and empname: {empname} is added successfully!")
        print("List of employees:")
        for idx, emp in enumerate(employees, start=1):
            print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}")
    elif choice == '2':
        if not employees:
            print("No employees available.")
        else:
            print("\nList of Employees:")
            for idx, emp in enumerate(employees, start=1):
                print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}")

    elif choice == '3':
        empno = int(input("Enter Employee Number to remove: "))
        removed = False
        for emp in employees[:]:  
            if emp['empno'] == empno:
                employees.remove(emp)
                removed = True
        if removed:
            print(f"Employee with EmpNo {empno} was removed successfully.")
            print("List of employees:")
            for idx, emp in enumerate(employees, start=1):
                print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}")
        else:
            print(f"No employee found with EmpNo {empno}.")
    elif choice == '4':
        print("List of employees before update:")
        for idx, emp in enumerate(employees, start=1):
            print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}")
        print(" ")

        empno = int(input("Enter Employee Number to update: "))
        print(" ")

        found = False
        for emp in employees:
            if emp['empno'] == empno:
                emp['empno'] = int(input("Enter Updated Employee Number: "))
                emp['empname'] = input("Enter Updated Employee Name: ")
                emp['designation'] = input("Enter Updated Designation: ")
                found = True
                print(" ")
                print("Employee Updated Successfully.")
                print(" ")
                break
        if not found:
            print(f"No employee found with EmpNo {empno}.")

        print("List of employees after update:")
        for idx, emp in enumerate(employees, start=1):
            print(f"{idx}. EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}")
    elif choice == '5':
        empno = int(input("Enter Employee Number to search: "))  
        found = False  
        for emp in employees:  
            if emp['empno'] == empno:  
                print(f"EmpNo: {emp['empno']}, EmpName: {emp['empname']}, Designation: {emp['designation']}")  
                found = True  
                break  
        if not found:  
            print(f"No employee found with EmpNo {empno}.")  
    elif choice == '6':
        print("Exiting Employee Management. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")