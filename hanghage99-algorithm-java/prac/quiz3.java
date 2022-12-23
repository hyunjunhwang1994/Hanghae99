package prac;

import java.util.ArrayList;

public class quiz3 {
    public void solution(int[][] arr1) {

        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        int len = arr1.length;


        boolean sw = false;

        for(int i = 0; i<len; i++){
            for(int j = 0; j<len; j++){

                for(int k=0; k<4; k++){
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    // 상 -> 우 -> 하 -> 좌

                    if(nx >= 0 && nx < len && ny >= 0 && ny < len && arr1[nx][ny] >= arr1[i][j]){

                        System.out.print(arr1[i][j]);
                        sw = false;
                        break;

                    }
                    sw = true;

                }
                if(sw == true){
                    System.out.print("*");
                }
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {
        quiz3 method = new quiz3();
        int[][] arr1 = {{3,4,1,4,9}, {2,9,4,5,8}, {9,0,8,2,1}, {7,0,2,8,4}, {2,7,2,1,4}};

        method.solution(arr1);
    }
}