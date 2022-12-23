public class Main {
    public static void main(String[] args) {

        PublicTransport bus1 = new Bus(1);
        PublicTransport bus2 = new Bus(2);

        bus1.boardingPassengers(2);

        bus1.setGasStatus(-50);
        bus1.getGasStatus();

        bus1.setStatus(false);
        bus1.isStatus();

        bus1.setGasStatus(10);
        bus1.getGasStatus();

        bus1.setStatus(true);


        bus1.boardingPassengers(45);
        bus1.boardingPassengers(5);

        bus1.setGasStatus(-55);
        bus1.getGasStatus();
        bus1.isStatus();




    }
}