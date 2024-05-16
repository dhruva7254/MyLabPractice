package code;
public class Book 
{
	private int bookId;
	private String name;
	private String author;
	private int price;
	public Book()
	{
		bookId = 123;
		name = "qwe";
		author = "asd";
		price = 456;
	}
	public Book(int b, String n, String a, int p)
	{
		bookId = b;
		name = n;
		author = a;
		price = p;
	}
	public int getbookId()
	{
		return bookId;
	}
	public String getname()
	{
		return name;
	}
	public String getauthor()
	{
		return author;
	}
	public int getprice()
	{
		return price;
	}
	public void setbookId(int bookId)
	{
		this.bookId=bookId;
	}
	public void setname(String name)
	{
		this.name=name;
	}
	public void setauthor(String author)
	{
		this.author=author;
	}
	public void setprice(int price)
	{
		this.price=price;
	}
	public void showBook()
	{
		System.out.println(bookId+" "+name+" "+author+" "+price);
	}
}