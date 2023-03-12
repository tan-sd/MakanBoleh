<template>
    <div class="container-fluid bg-dark text-light" id="login-body">
        <img src="../assets/images/logos/large_logos/MakanBoleh_logo_stacked_light_large.png" class="logo_img">

        <form action="" class="d-flex flex-column mt-4">
            <small>Username</small>
            <input type="text">

            <small>Password</small>
            <input type="password">

            <div class="d-flex justify-content-center">
                <button class="btn btn-main mt-3">Login</button>
            </div>
        </form>
    </div>
</template>


<script>
    export default{
        data() {
            return {

            }
        }
    }
</script>


<style scoped>
    #login-body{
        height: 100vh;
        height: 100svh;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }

    .logo_img{
        width: 250px
    }
</style>