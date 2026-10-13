
class NonTechnicalLossDetectionSystem:
    def __init__(self, supplied_energy, recorded_energy,
                 loss_limit, meter_status):
        self.supplied_energy = supplied_energy
        self.recorded_energy = recorded_energy
        self.loss_limit = loss_limit
        self.meter_status = meter_status

    def calculate_energy_difference(self):
        return self.supplied_energy - self.recorded_energy

    def calculate_loss_percentage(self):
        if self.supplied_energy <= 0:
            return 0

        difference = self.calculate_energy_difference()
        return (difference / self.supplied_energy) * 100

    def detect_loss(self):
        difference = self.calculate_energy_difference()
        loss_percentage = self.calculate_loss_percentage()

        if self.supplied_energy <= 0 or self.recorded_energy < 0:
            return "INVALID DATA"

        if difference < 0:
            return "CHECK METER DATA"

        if self.meter_status.lower() != "normal":
            return "METER INSPECTION REQUIRED"

        if loss_percentage > self.loss_limit:
            return "POSSIBLE NON-TECHNICAL LOSS"

        return "NORMAL"

    def display_result(self):
        difference = self.calculate_energy_difference()
        loss_percentage = self.calculate_loss_percentage()
        status = self.detect_loss()

        print("----- Non-Technical Loss Detection System -----")
        print(f"Supplied Energy   : {self.supplied_energy:.2f} kWh")
        print(f"Recorded Energy   : {self.recorded_energy:.2f} kWh")
        print(f"Energy Difference : {difference:.2f} kWh")
        print(f"Loss Percentage   : {loss_percentage:.2f}%")
        print(f"Meter Status      : {self.meter_status}")
        print(f"Detection Result  : {status}")

        if status == "POSSIBLE NON-TECHNICAL LOSS":
            print("Alert: Investigate the energy discrepancy.")
        elif status == "METER INSPECTION REQUIRED":
            print("Alert: Inspect the meter and its connections.")
        elif status == "NORMAL":
            print("Energy difference is within the set limit.")


# Example input values
supplied_energy = 1000     # kWh
recorded_energy = 920      # kWh
loss_limit = 5             # Percentage
meter_status = "normal"

system = NonTechnicalLossDetectionSystem(
    supplied_energy,
    recorded_energy,
    loss_limit,
    meter_status
)

system.display_result()
