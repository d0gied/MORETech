import { YMaps, Map } from "@pbe/react-yandex-maps"
import SideBar from "./components/sidebar"
import Topbar from "./components/topbar"
import MobileDrawer from "./components/mobileDrawer"
import CustomDrawer from "./components/CustomDrawer"

export default function App() {
    return (
        <YMaps>
            <div className="ui-wrapper">
                <Topbar />
                {/* <MobileDrawer /> */}
                {/* <SideBar/> */}
                <CustomDrawer/>
            </div>

            <Map
                defaultState={{
                    center: [55.75, 37.57],
                    zoom: 9
                }}
                className="map-container"
            />
        </YMaps>
    )
}
