import type { Route } from "./+types/home";
import { Welcome } from "../welcome/welcome";

export function meta({}: Route.MetaArgs) {
  return [
    { title: "Hackamail" },
    { name: "description", content: "Welcome to the work-in-progress website for Hackamail!" },
  ];
}

export function loader({ context }: Route.LoaderArgs) {
  return { message: "Hackamail is a Hack Club YSWS Program. Hack Club is a global nonprofit network of high school makers & student-led coding clubs where young people build the agency, the network, & the technical talent to think big & do big things in the world. Founded in 2014 by 16-year-old Zach Latta, Hack Clubs are now in nearly 400 high schools with 10,000 students each year." };
}

export default function Home({ loaderData }: Route.ComponentProps) {
  return <Welcome message={loaderData.message} />;
}
