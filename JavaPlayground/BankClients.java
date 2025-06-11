import java.util.Scanner;

class BankClients{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number;
        do {
            number = scanner.nextInt();
            switch (number) {
                case 1:
                    System.out.println("Language selection");
                    continue;
                case 2:
                    System.out.println("Customer support");
                    continue;
                case 3:
                    System.out.println("Check the balance");
                    continue;
                case 0:
                    System.out.println("Exit");
                    break;
            }
        }

        while(number != 0);

    }
}