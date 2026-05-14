import { NextResponse } from "next/server";
import fs from "fs";
import path from "path";

const productsFile = path.join(process.cwd(), "app", "product.json");

// ================= GET =================

export async function GET() {

  // Read product.json file
  const data = fs.readFileSync(productsFile, "utf8");

  // Convert string to JavaScript array
  const products = JSON.parse(data);

  // Return products
  return NextResponse.json(products);
}





// ================= POST =================

export async function POST(request) {

  // Read new product from request body
  const newProduct = await request.json();

  // Read old products
  const data = fs.readFileSync(productsFile, "utf8");

  const products = JSON.parse(data);

  // Add new product
  products.push(newProduct);

  // Save updated products
  fs.writeFileSync(
    productsFile,
    JSON.stringify(products, null, 2)
  );

  // Return response
  return NextResponse.json({
    message: "Product added successfully",
    products
  });
}





// ================= PUT =================

export async function PUT(request) {

  // Read updated product
  const updatedProduct = await request.json();

  // Read existing products
  const data = fs.readFileSync(productsFile, "utf8");

  const products = JSON.parse(data);

  // Update matching product
  const updatedProducts = products.map((product) =>
    product.id === updatedProduct.id
      ? updatedProduct
      : product
  );

  // Save updated data
  fs.writeFileSync(
    productsFile,
    JSON.stringify(updatedProducts, null, 2)
  );

  // Return response
  return NextResponse.json({
    message: "Product updated successfully",
    updatedProducts
  });
}





// ================= DELETE =================

export async function DELETE(request) {

  // Read id from body
  const body = await request.json();

  // Read old products
  const data = fs.readFileSync(productsFile, "utf8");

  const products = JSON.parse(data);

  // Remove matching product
  const filteredProducts = products.filter(
    (product) => product.id !== body.id
  );

  // Save updated products
  fs.writeFileSync(
    productsFile,
    JSON.stringify(filteredProducts, null, 2)
  );

  // Return response
  return NextResponse.json({
    message: "Product deleted successfully",
    filteredProducts
  });
}