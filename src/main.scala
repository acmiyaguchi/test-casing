import scala.io.StdIn
import com.google.common.base.CaseFormat;

object Main extends App {
    var line: String = null;
    while ({line = StdIn.readLine(); line} != null) {
        println(CaseFormat.LOWER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, line));
    }
}
