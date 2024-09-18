import android.content.Context
import androidx.room.Room
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object RoomModule {

    @Provides
    @Singleton
    fun providesDatabase(@ApplicationContext context: Context): Database =
        Room.databaseBuilder(
            context,
            Database::class.java,
            Constants.DATABASE_NAME
        ).fallbackToDestructiveMigrationFrom().build()

    @Provides
    @Singleton
    fun providesDao(Database: Database): Dao =
        Database.Dao()
}