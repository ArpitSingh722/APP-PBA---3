class Parcel:
    def __init__(self, parcel_id, sender_name, parcel_weight):
        self.parcel_id = parcel_id
        self.sender_name = sender_name
        self.parcel_weight = float(parcel_weight)
        self.category = self.categorize_parcel()

    def categorize_parcel(self):
        if self.parcel_weight < 2.0:
            return "Light"
        elif 2.0 <= self.parcel_weight <= 10.0:
            return "Medium"
        else:
            return "Heavy"

    def display_info(self):
        print(
            f"{self.parcel_id:<12} | {self.sender_name:<20} | "
            f"{self.parcel_weight:<10.2f} | {self.category:<10}"
        )


class CourierService:
    def __init__(self, service_name="SwiftTrack Couriers"):
        self.service_name = service_name
        self.parcels = []

    def add_parcel(self, parcel_id, sender_name, parcel_weight):
        if any(p.parcel_id == parcel_id for p in self.parcels):
            print(f"\n[Error] Parcel ID '{parcel_id}' already exists in records.")
            return

        new_parcel = Parcel(parcel_id, sender_name, parcel_weight)
        self.parcels.append(new_parcel)
        print(
            f"\n[Success] Parcel '{parcel_id}' ({new_parcel.category}) added to records."
        )

    def display_all_parcels(self):
        print(f"\n--- {self.service_name}: Maintained Parcel Records ---")
        if not self.parcels:
            print("No parcel records found.")
            return

        print("-" * 62)
        print(
            f"{'Parcel ID':<12} | {'Sender Name':<20} | {'Weight(kg)':<10} | {'Category':<10}"
        )
        print("-" * 62)
        for parcel in self.parcels:
            parcel.display_info()
        print("-" * 62)
        print(f"Total Parcels Maintained: {len(self.parcels)}\n")


def main():
    courier = CourierService()

    while True:
        print("\n=== Courier Parcel Management System ===")
        print("1. Add Parcel Details")
        print("2. Display All Parcels")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            p_id = input("Enter Parcel ID: ").strip()
            sender = input("Enter Sender Name: ").strip()
            try:
                weight = float(input("Enter Parcel Weight (in kg): "))
                if weight <= 0:
                    print("[Error] Weight must be greater than 0.")
                else:
                    courier.add_parcel(p_id, sender, weight)
            except ValueError:
                print("[Error] Please enter a valid numeric weight.")

        elif choice == "2":
            courier.display_all_parcels()

        elif choice == "3":
            print("Exiting system...")
            break

        else:
            print("[Error] Invalid choice. Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
