package Date221231;


// 2022 12월 31일
// https://school.programmers.co.kr/learn/courses/30/lessons/12949
// https://www.youtube.com/watch?v=JpSe38UHaos <- 행렬의 곱셈 수학 유튜브
// 행렬의 곱셈.


public class Main {



    public int[][] solution(int[][] arr1, int[][] arr2) {



        int arr1row = arr1.length;
        int arr2col = arr2[0].length;
        int sum = 0;

        int[][] answer = new int[arr1row][arr2col];


        for (int i = 0; i<arr1row; i++){

            for (int j = 0; j < arr2col; j++) {

                // [0][0] * [0][0]
                // [0][1] * [1][0]
                // [0][2] * [2][0]

                // [0][0] * [0][1]
                // [0][1] * [1][1]
                // [0][2] * [2][1]

                // [0][0] * [0][2]
                // [0][1] * [1][2]
                // [0][2] * [2][2]

                // [1][0] * [0][0]
                // [1][1] * [1][0]
                // [1][2] * [2][0]

                // [1][0] * [0][1]
                // [1][1] * [1][1]
                // [1][2] * [2][1]

                // [1][0] * [0][2]
                // [1][1] * [1][2]
                // [1][2] * [2][2]


                System.out.println(i + "row, " +  j + "column");
                for (int k = 0; k < arr2.length; k++) {


                     sum += arr1[i][k] * arr2[k][j];


                }
                answer[i][j] = sum;
                sum = 0;

            }


        }


        return answer;
    }


    public static void main(String[] args) {

        int[][] arr1 = {{1, 4}, {3, 2}, {4, 1}};
        int[][] arr2 = {{3, 3}, {3, 3}};


        Main main = new Main();

        System.out.println(main.solution(arr1, arr2));




    }
}