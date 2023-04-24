# Doodle Hub


Doodle Hub is a free and open source doodle sharing platform where you can draw and receive doodles anonymously.

## Features

- Receive doodles anonymously
- View all the doodles you have received in the past
- Receive email notifications when you receive a doodle
- Draw doodles on the drawing board

## Self-hosting

You can self-host DoodleHub on your own server using Docker. 

### Requirements

- Docker
- Supabase Account 
- Courier Account


### Instructions

1. Clone the repository

```bash
git clone https://github.com/n4ze3m/doodle-hub.git
```

2. Setup Supabase and Courier

#### Setup Supabase

a. Create a new project in Supabase
b. Use `SUPABASE.sql` to create the required tables and functions in Supabase Query Editor.
c. Copy paste the URL and Anon Key from the Supabase project settings page.
d. Please enable google auth in the Supabase project settings page. Refer to [this](https://supabase.com/docs/guides/auth/social-login/auth-google) for more details.

#### Setup Courier

a. Create a new template in Courier
b. In template add following variables:

- `{{img}}` - Doodle image URL
- `{{username}}` - Doodle sender name

c. Copy paste the API Key and Template ID from the Courier project settings page.



3. Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
# Supabase URL
SUPABASE_URL=
# Supabase Anon Key
SUPABASE_KEY=
# Courier API Key
COURIER_AUTH_TOKEN=
# Courier API Secret
COURIER_TEMPLATE_ID=
```

4. Run the following command to start the server:

```bash
docker compose up -d
```

5. Open `http://localhost:3334` in your browser to view the app.


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](LICENSE)