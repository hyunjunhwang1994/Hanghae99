public class Taxi extends PublicTransport{

    int currentPassengers = 1;
    int maxPassengers = 30;
    int fare = 8000;
    int number;
    boolean status;

    int gasMileage;


    public Taxi(int number) {
        this.status = true;
        this.number = number;
        System.out.println(number + "번 택시객체 만들어짐!");

    }

    @Override
    public int getGasStatus() {
        return super.getGasStatus();
    }

    @Override
    public void setGasStatus(int gasStatus) {
        super.setGasStatus(gasStatus);
    }

    @Override
    public void setChangeSpeed(int changeSpeed) {
        super.setChangeSpeed(changeSpeed);
    }

    @Override
    public void setStatus(boolean status) {
        super.setStatus(status);
    }

    @Override
    public int getNumber() {
        return super.getNumber();
    }

    @Override
    public boolean isStatus() {
        return super.isStatus();
    }

    @Override
    public void boardingPassengers(int passengersNumber) {
        super.boardingPassengers(passengersNumber);
    }
}
