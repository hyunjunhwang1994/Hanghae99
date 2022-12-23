public class Prac04_1 {

    public static void main(String[] args) {



        int[][] array ={
                {95, 86},
                {83, 92, 96},
                {78, 83, 93, 87, 88}
        };

        int sum=0;
        double avg =0.0;
        int count = 0;

        for(int i = 0; i < array.length; i++){

            for(int x = 0; x < array[i].length; x++){

                sum += array[i][x];
                ++count;

            }
        }
        avg = sum / count;

        System.out.println("sum : " + sum);
        System.out.println("avg : " + avg);
        System.out.println("cnt : " + count);




    }



}
