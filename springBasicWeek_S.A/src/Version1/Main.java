package Version1;

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
        System.out.println("==================");


        PublicTransport taxi1 = new Taxi(1);
        PublicTransport taxi2 = new Taxi(2);


        taxi1.getGasStatus();
        taxi1.isStatus();

        taxi1.boardingPassengers(2, "서울역", 2);

        taxi1.isStatus();
        taxi1.setGasStatus(-80);


        taxi1.bill();

        taxi1.boardingPassengers(5);

        taxi1.boardingPassengers(3,"구로디지털단지역",12);


        taxi1.setGasStatus(-20);
        taxi1.bill();

        taxi1.isStatus();


    }
}