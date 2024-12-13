import { writable } from "svelte/store";
import axios from "axios";

export const users = writable([]);
export const loading = writable(true);

export async function fetchUsers() {
  try {
    loading.set(true);
    const response = await axios.get("http://127.0.0.1:5000/api/users");
    users.set(response.data);
  } catch (error) {
    console.error("Erreur lors de la récupération des utilisateurs :", error);
  } finally {
    loading.set(false);
  }
}
