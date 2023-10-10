import { SwipeableDrawer, Box, Typography, Skeleton, Button } from "@mui/material"
import { styled } from "@mui/material/styles"
import { useState } from "react"

const drawerBleeding = 56

const Puller = styled(Box)(() => ({
    width: 100,
    height: 7,
    backgroundColor: "#909090",
    borderRadius: 3,
    position: "absolute",
    top: 0,
    left: "calc(50% - 50px)"
}))

const container =  document.body

export default function MobileDrawer() {
    const [open, setOpen] = useState(false)

    const toggleDrawer = (newOpen: boolean) => () => {
        setOpen(newOpen)
        console.log("123123")
    }

    return (
        <div className="mobile-drawer">

            <Box sx={{ textAlign: "center", pt: 1 }}>
                <Button >Open</Button>
            </Box>
            <SwipeableDrawer
                container={container}
                anchor="bottom"
                open={open}
                onClose={toggleDrawer(false)}
                onOpen={toggleDrawer(true)}
                swipeAreaWidth={drawerBleeding}
                disableSwipeToOpen={false}
                ModalProps={{
                    keepMounted: true
                }}
            >
                <Box
                    sx={{
                        position: "absolute",
                        top: 10,
                        borderTopLeftRadius: 32,
                        borderTopRightRadius: 32,
                        visibility: "visible",
                        right: 0,
                        left: 0,
                        height: "100vh",
                        backgroundColor: "#ffffff"
                    }}
                >
                    
                <Puller />
                </Box>
                <Box
                    sx={{
                        backgroundColor: "#ffffff",
                        px: 2,
                        pb: 2,
                        height: "50vh",
                        overflow: "auto"
                    }}
                >
                    <Skeleton variant="rectangular" height="100%" />
                </Box>
            </SwipeableDrawer>
        </div>
    )
}
