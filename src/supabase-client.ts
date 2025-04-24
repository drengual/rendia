import { createClient } from "@supabase/supabase-js";

const supabaseUrl = "https://bvohpetyejykqhlonuzo.supabase.co";
//process.env.NEXT_PUBLIC_SUPABASE_URL as string;

const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY as string;

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
