import Link from "next/link";

export default function RootLayout({ children }) {
    return(
    <html>
        <body>
            <nav style={{padding:"20px",background:"#eee"}}>
                <Link href="/" style={{marginRight:"10px"}}>Home</Link>
                <Link href="/about" style={{marginRight:"10px"}}>About</Link>
                <Link href="/contact" style={{marginRight:"10px"}}>Contact</Link>
                <Link href="/users/1" style={{marginRight:"10px"}}>USER 1</Link>

            </nav>
            <div style={{padding:"20px"}}>
                {children}

            </div>
        </body>
    </html>
    );
}

