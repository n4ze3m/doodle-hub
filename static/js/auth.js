const hash = window.location.hash;

if (hash.includes("#access_token=")) {
    const accessToken = hash.split("=")[1];
    document.cookie = `supabase_access_token=${accessToken}; path=/`;
    window.history.replaceState(null, null, window.location.pathname);

    console.log("Access token saved to cookie");
}
