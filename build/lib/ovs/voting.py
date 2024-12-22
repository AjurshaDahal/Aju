from .db_connection import connect_db

def vote_for_party(voter_id):
    print("Login Successful! You can now vote.")
    print("Please choose a party to vote for:")
    print("1. Party A")
    print("2. Party B")
    print("3. Party C")

    choice = input("Enter the party number: ")

    party_name = ""
    if choice == '1':
        party_name = "Party A"
    elif choice == '2':
        party_name = "Party B"
    elif choice == '3':
        party_name = "Party C"
    else:
        print("Invalid choice.")
        return

    try:
        connection = connect_db()
        if connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO votes (voter_id, party_name) VALUES (%s, %s)", (voter_id, party_name))
            connection.commit()
            print(f"Vote for {party_name} by Voter ID {voter_id} recorded successfully.")
            cursor.close()
            connection.close()
    except Exception as e:
        print(f"Database error: {e}")
