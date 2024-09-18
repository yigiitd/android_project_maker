import androidx.room.Database
import androidx.room.RoomDatabase

@Database(
    entities = [Dto::class],
    version = 1,
    exportSchema = false
)
abstract class Database : RoomDatabase() {
    abstract fun Dao(): Dao
}