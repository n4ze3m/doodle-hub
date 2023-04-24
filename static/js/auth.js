const hash = window.location.hash;


if (hash.includes("#access_token=")) {
    const accessToken = hash.split("=")[1].replace("&expires_in", "");
    const expiresIn = hash.split("&")[1].split("=")[1];
    const providerToken = hash.split("&")[2].split("=")[1];
    const refreshToken = hash.split("&")[3].split("=")[1];

    document.cookie = `supabase_access_token=${accessToken}; path=/; expires=${new Date(
        new Date().getTime() + expiresIn * 1000
    ).toUTCString()}`;

    document.cookie = `supabase_refresh_token=${refreshToken}; path=/; expires=${new Date(
        new Date().getTime() + expiresIn * 1000
    ).toUTCString()}`;

    document.cookie = `supabase_provider_token=${providerToken}; path=/; expires=${new Date(
        new Date().getTime() + expiresIn * 1000
    ).toUTCString()}`;

    // window.history.replaceState(null, null, window.location.pathname);
    window.location.href = "/dashboard";
    console.log("Access token saved to cookie");
}

const currentPath = window.location.pathname;

if (currentPath === "/") {
    if (document.cookie.includes("supabase_access_token")) {
        window.location.href = "/dashboard";
    }
}