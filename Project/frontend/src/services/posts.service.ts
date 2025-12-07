import { api } from "./api";

export async function getMarketplacePosts() {
  const response = await api.get("/posts/marketplace/");
  return response.data;
}

