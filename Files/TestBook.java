package tester;
import code.Book;
import java.util.Scanner;
public class TestBook 
{
	public static void main(String[] args) 
	{
		Book bookobj1 = new Book();
		bookobj1.showBook();
		Book bookobj2 = new Book(198,"qaz","wsx",167);
		bookobj2.showBook();
		System.out.println("1:Show All Books "+
				           "2:Add New Book "+
				           "3:Update Book "+
				           "4:Delete Book "+
				           "5:Edit Name "+
				           "6:Edit Author "+
				           "7:Edit Price ");
		Scanner sc = new Scanner(System.in);
		int ch;
//		Book bookobj3=null;
		do
		{
			System.out.print("Enter your Choice ");
			ch = sc.nextInt();
			switch (ch) 
			{
				case 1:
					bookobj2.showBook();
					break;
				case 2:
					System.out.println("bookId name author price");
					bookobj2 = new Book(sc.nextInt(), sc.next(), sc.next(), sc.nextInt());
					bookobj2.showBook();
					break;
				case 3:
					System.out.println("Enter new bookId: ");
					int a=sc.nextInt();
					bookobj2.setbookId(a);
					System.out.println("Enter new name: ");
					String b=sc.next();
					bookobj2.setname(b);
					System.out.println("Enter new author: ");
					String c=sc.next();
					bookobj2.setauthor(c);
					System.out.println("Enter new price: ");
					int d=sc.nextInt();
					bookobj2.setprice(d);
					bookobj2.showBook();
					break;
				case 4:
					bookobj2.setbookId(0);
					bookobj2.setname("null");
					bookobj2.setauthor("null");
					bookobj2.setprice(0);
					bookobj2.showBook();
					break;
				case 5:
					System.out.println("Enter new name: ");
					String e=sc.next();
					bookobj2.setname(e);
					bookobj2.showBook();
					break;
				case 6:
					System.out.println("Enter new author: ");
					String f=sc.next();
					bookobj2.setauthor(f);
					bookobj2.showBook();
					break;
				case 7:
					System.out.println("Enter new price: ");
					int g=sc.nextInt();
					bookobj2.setprice(g);
					bookobj2.showBook();
					break;
				default:
					System.out.println("Enter valid choice <= 7 !!!");
			}
		}
		while(ch!=8);
		sc.close();
	}
}