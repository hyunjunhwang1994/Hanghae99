package hj.homework01;

public class Exam {

    public static void main(String[] args) {

        method(new LoginServlet());
        method(new FileDownloadServlet());

    }

    public static void method(HttpServlet servlet){
        servlet.service();
    }

}
