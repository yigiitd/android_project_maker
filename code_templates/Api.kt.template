import retrofit2.http.GET
import retrofit2.http.Query

interface Api {

    @GET("")
    suspend fun getStations(
        @Query("") key: String = "",
    ): Dto
}