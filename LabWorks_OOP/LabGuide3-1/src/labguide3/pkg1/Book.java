
package labguide3.pkg1;

public class Book {
    String title;
    int publish_year;
    double price;
    
    public Book(){
        title = "NoBookTitle";
        publish_year = 0;
        price = 0;
    }

    public Book(String title, int publish_year, double price) {
        this.title = title;
        this.publish_year = publish_year;
        this.price = price;
    }
    
    public void display(){
        System.out.println(title);
        System.out.println(publish_year);
        System.out.println(price);
    }
   
}
