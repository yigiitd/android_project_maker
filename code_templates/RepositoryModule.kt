import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object RepositoryModule {

    @Provides
    @Singleton
    fun providesRepository(
        Api: Api,
        Dao: Dao,
    ): RepositoryImpl =
        RepositoryImpl(
            Api = Api,
            Dao = Dao,
        )
}