
package labguide3_2;

public class BookClass {
    String title;
    int publish_year;
    double price;

    public BookClass(String title, int publish_year, double price) {
        this.title = title;
        this.publish_year = publish_year;
        this.price = price;
    }

    public BookClass(String title, int publish_year) {
        this.title = title;
        this.publish_year = publish_year;
    }

    public BookClass(String title) {
        this.title = title;
    }

    public BookClass() {
        title = "NoBookTitle";
        publish_year = 0;
        price = 0;
    }
    
    public void display(){
        System.out.printf(title + " , " + publish_year + " ," + price + "TL"+"\n");
    }
    
}
