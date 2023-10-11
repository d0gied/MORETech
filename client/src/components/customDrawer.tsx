import { PropsWithChildren, useState, MouseEvent, useEffect } from "react"

const drawerAnchors = {

}

export default function CustomDrawer(props: PropsWithChildren) {
    const [pullable, setPullable] = useState<Boolean>(false)
    const [targetY, setTargetY] = useState(0);
    const [startY, setStartY] = useState(0);
    const [drawerPositionStyles, setDrawerPositionStyles] = useState({
        transform: "translateY(0)",
        transition: "none",
    })

    useEffect(() => {
        console.log(pullable)
        if (pullable == false) {
            const y = Math.max(window.innerHeight / 4, (Math.round(targetY / window.innerHeight * 4) - 1) * (window.innerHeight / 4))
            console.log(targetY, y)
            setDrawerPositionStyles({
                transform: "translateY("+(y)+"px)",
                transition: "transform 0.2s",
            })
        }
    }, [pullable])

    const pullDrawer = (event: MouseEvent<HTMLElement>) => {
        if (startY == 0) setStartY(event.clientY)
        else if (pullable) {
            //console.log(event.clientY, startY)
            const y = event.clientY - startY + 32
            setDrawerPositionStyles({
                transition: "none",
                transform: "translateY("+(y)+"px)"
            })
            setTargetY(event.clientY)
        }
    }

    return (
        <div className="custom-drawer" style={drawerPositionStyles}>
            <div 
                onMouseMove={(event) => { pullDrawer(event) }} 
                onMouseDown={() => { setPullable(true) }} 
                onMouseUp={() => {setPullable(false)}} 
                className="puller"
                onMouseLeave={() => {setPullable(false)}} 
            >
            </div>
            {props.children}
        </div>
    )
}
