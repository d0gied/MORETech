import logo from "../assets/vtb-logo.svg"
import { Link } from "react-router-dom"

export default function Topbar() {
    return (
        <div className="topbar-wrapper">
            <a href="https://online.vtb.ru/" className="logo-wrapper">
                <img className="logo" src={logo} />
            </a>
        </div>
    )
}

