import java.util.Scanner;

public class feet2Inches {
    static void convert(double number) {
        System.out.println("Measurement in inches is " + number * 12);
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
	System.out.println("Provide measurement in feet: ");
	double num = sc.nextDouble(); 

        convert(num);
	sc.close();
    }
}
