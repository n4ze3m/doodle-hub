DROP TABLE IF EXISTS "Submissions";
CREATE TABLE "public"."Submissions" (
    "id" uuid DEFAULT extensions.uuid_generate_v4() NOT NULL,
    "user_id" uuid,
    "img" text,
    "created_at" timestamptz DEFAULT now(),
    CONSTRAINT "Submissions_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


DROP TABLE IF EXISTS "User";
CREATE TABLE "public"."User" (
    "id" uuid NOT NULL,
    "email" text,
    "created_at" timestamptz DEFAULT now(),
    "block_incoming" boolean DEFAULT false,
    "email_notification" boolean DEFAULT true,
    "public_id" uuid DEFAULT extensions.uuid_generate_v4(),
    "raw_user_meta_data" jsonb,
    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
) WITH (oids = false);


ALTER TABLE ONLY "public"."Submissions" ADD CONSTRAINT "Submissions_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "User"(id) NOT DEFERRABLE;

create or replace function public.handle_new_user() 
returns trigger as $$
begin
  insert into public."User" ("id", email, raw_user_meta_data)
  values (new.id, new.email, new.raw_user_meta_data);
  return new;
end;
$$ language plpgsql security definer;

create trigger on_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();


insert into storage.buckets
  (id, name)
values
  ('images', 'images');

