import cv2

WINDOW_NAME = "image"
CROP_WINDOW_NAME = "cropped"

cv2.namedWindow(WINDOW_NAME)
image = cv2.imread('./images/khwarizmy.jpg')

POINTS = []
clone = image.copy()


def mouse_callback(event, x, y, flags, param):
    """
    يتم مناداة الدالة كل مرة تتحرك فيا الفأرة
    او يتم الضغط على اى زر فيها

    Arguments:
        event : حالة الفأرة
        x : الاحداثى الأفقى
        y : الاحداثى الرأسى
        flags : معلومات اضافية
        param : اعدادات او قيم تريد استخدامها
    """

    global clone

    # * تم الضغط على زر الفأرة الأيسر
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.destroyWindow(CROP_WINDOW_NAME)
        clone = image.copy()
        POINTS.append((x, y))
        # cv2.circle(clone, (x, y), 30, param['green'], -1)

    # * تم رفع الاصبع عن زر الفأرة الأيسر
    if event == cv2.EVENT_LBUTTONUP:
        POINTS.append((x, y))


colors = {'red': (0, 0, 255), 'green': (0, 255, 0)}

cv2.setMouseCallback(WINDOW_NAME, mouse_callback, param=colors)

while True:

    cv2.imshow(WINDOW_NAME, clone)

    if len(POINTS) == 2:
        cv2.rectangle(clone, *POINTS, (0, 0, 255), 3)

        # * جعل قيم السينات مع بعض
        # * وجعل قيم الصادات مع بعض
        xs, ys = zip(*POINTS)

        cv2.imshow(CROP_WINDOW_NAME,
                   #!  لان لو حاولت ان تكون المستطيل من اليمن لليسار
                   #! أو من اسفل لاعلى سيحدث خطأ لان النهاية اقل من البدية
                   #! فى قيم السينات او الصادات او كليهما
                   clone[min(ys):max(ys), min(xs):max(xs)]
                   #    clone[POINTS[0][1]:POINTS[-1][1],
                   #          POINTS[0][0]:POINTS[-1][0]]
                   )

        POINTS = []

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.waitKey(0)
