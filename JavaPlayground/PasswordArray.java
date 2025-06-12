import java.util.Scanner;

class PasswordArray{
    public static void main(String[] args) {
        
        int[] passwords = {2021, 1023, 9929};
        Scanner scanner = new Scanner(System.in);

	System.out.println("Please enter password: ");
        int  password = scanner.nextInt();
	
        for (int x : passwords) {
            if (password == x) {
                System.out.println("Welcome");
            } else {
                continue;
            }
        }
    }
}
