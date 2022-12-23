package Version2_Interface;

public class Main {


    public static void main(String[] args) {
        PublicTransport bus1 = new Bus(1);
        PublicTransport bus2 = new Bus(2);


        bus1.boardingPassengers(2);

        bus1.fillUp(-50);
        bus1.showFual();

        bus1.changeStatus();
        bus1.fillUp(10);

        bus1.showStatus();
        bus1.showFual();

        bus1.changeStatus();

        bus1.boardingPassengers(45);

        bus1.boardingPassengers(5);

        bus1.fillUp(-55);

        bus1.showFual();
        bus1.showStatus();



    }
}
