from pytube import Search

def search_youtube(query):
    try:
        search = Search(query)
        results = [f"https://www.youtube.com/watch?v={video.video_id}" for video in search.results[:5]]
        return results
    except Exception as e:
        return f"Error searching YouTube: {e}"
